"""
Includes mock tests for API and path tests for each individual unit (class) and its methods.
"""

import unittest
from unittest import mock
from unittest.mock import patch
import json
import sys
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))

from view.appView import AppView
from model.apiRequestHandler import APIRequestHandler
from controller.appController import AppController


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


def test_get_one_ticket(url="", auth=""):
    f2 = open('data (1).json', 'r')  # Sample json ticket data for one ticket
    j2 = json.load(f2)
    mockObject = MockResponse(j2, 200)
    return mockObject


def test_get_all_tickets(url="", auth=""):  # Sample json ticket data for bulk tickets
    f1 = open('data.json', 'r')
    j1 = json.load(f1)
    mockObject = MockResponse(j1, 200)
    return mockObject


def test_get_bad_request_response(url="", auth=""):  # Sample json ticket data for bulk tickets
    f1 = open('data.json', 'r')
    j1 = json.load(f1)
    mockObject = MockResponse(j1, 400)
    return mockObject


class TicketViewerTester(unittest.TestCase):
    @patch('model.apiRequestHandler.requests.get', side_effect=test_get_one_ticket)
    # replace requests.get with my dummy function to simulate API call/request.
    def test_api_get_one(self, test_get):  # mocking api interaction
        api = APIRequestHandler()
        ticket = api.getTicketByID(2)
        self.assertEqual(len(ticket), 1)
        assert "ticket" in ticket

    @patch('model.apiRequestHandler.requests.get', side_effect=test_get_all_tickets)
    # replace requests.get with my dummy function to to simulate API call/request.
    def test_api_get_all(self, test_get):  # mocking api interaction
        api = APIRequestHandler()
        ticket = api.getAllTickets()
        assert "tickets" in ticket
        print("Ticket Length: ", len(ticket["tickets"]))
        self.assertEqual(len(ticket["tickets"]), 100)

    @patch('model.apiRequestHandler.requests.get', side_effect=test_get_bad_request_response)
    # Test to get bad request from API, mocking the network access to simulate API call/request.
    def test_bad_request(self, test_get):
        api = APIRequestHandler()
        ticket = api.connectToAPI()
        self.assertEqual(ticket, False)  # api.connectToAPI returns on bad request

    # Testing basic functionality of view
    def test_view(self):
        j1 = test_get_one_ticket()
        j2 = test_get_all_tickets()
        view = AppView()
        self.assertEqual(view.printMenu(), 0)
        self.assertEqual(view.inputError(), 1)
        self.assertEqual(view.displaySingleTicket(j1.json_data), 0)
        self.assertEqual(view.displayTickets(j2.json_data, 1), 1)
        self.assertEqual(view.startMessage(), 0)
        self.assertEqual(view.ticketIDError(), 1)
        self.assertEqual(view.pageCommandError(), 1)

    @patch("builtins.input", return_value='q')  # Simulate user quitting correctly to test quitting functionality
    def test_user_quit(self, input):
        controller = AppController()
        with self.assertRaises(SystemExit) as cm:
            controller.showMainMenu()
        self.assertEqual(cm.exception.code, 0)

    # Simulate and test user inputs and related outputs to show all tickets then quit, followed by display all & paging.
    # ['1', 'q', 'd', 'q']:
    # Show all tickets (1) through menu then quit (q). Then display all and go down one page (d) & quit (q)
    @patch("builtins.input", side_effect=['1', 'q', 'd', 'q'])
    @patch('model.apiRequestHandler.requests.get', side_effect=test_get_all_tickets)
    def test_show_all(self, input, test_get):
        controller = AppController()
        with self.assertRaises(SystemExit) as cm:
            controller.showMainMenu()
        self.assertEqual(cm.exception.code, 0)
        with self.assertRaises(SystemExit) as cm:
            controller.showAllTickets()
        self.assertEqual(cm.exception.code, 0)
        self.assertEqual(controller.currPage, 2)  # We scrolled down one page, so checking if paging happened correctly.

    # Simulate and test user inputs for getting ticket ID's 2, 3 and 4 to get correct respective outputs.
    @patch("builtins.input", side_effect=['2', '3', '4'])
    @patch('model.apiRequestHandler.requests.get', side_effect=test_get_one_ticket)
    def test_show_one(self, input, test_get):
        controller = AppController()
        self.assertEqual(controller.showOneTicket(), 0)
        self.assertEqual(controller.currID, 2)
        self.assertEqual(controller.showOneTicket(), 0)
        self.assertEqual(controller.currID, 3)
        self.assertEqual(controller.showOneTicket(), 0)
        self.assertEqual(controller.currID, 4)

    def test_date_formatting(self):  # test date is formatted correctly
        api = APIRequestHandler()
        updated, created = api.formatDates("2017-11-13T12:34:23Z", "2017-10-13T12:34:23Z")
        self.assertEqual(updated, "2017-11-13 12:34:23")
        self.assertEqual(created, "2017-10-13 12:34:23")


if __name__ == "__main__":
    unittest.main()
    # TO-DO: report coverage after tests finish running.
