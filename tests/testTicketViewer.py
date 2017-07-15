'''
Includes mock tests for API and path tests for each individual unit (class) and its methods.
'''
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


class TicketViewerTester(unittest.TestCase):
    def test_api(self):
        # mocking api interaction
        api = APIRequestHandler()
        pass

    # Testing basic functionality of view
    def test_happy_path(self):
        f1 = open('data.json', 'r')
        j1 = json.load(f1)
        f2 = open('data (1).json', 'r')
        j2 = json.load(f2)
        f1.close()
        f2.close()
        view = AppView()
        self.assertEqual(view.printMenu(), 0)
        self.assertEqual(view.inputError(), 1)
        self.assertEqual(view.displaySingleTicket(j2), 0)
        self.assertEqual(view.displayTickets(j1, 1), 1)

        pass

        # few happy path tests

    @patch("builtins.input", return_value='q')  # q : quit
    def test_user_quit(self, input):
        controller = AppController()
        with self.assertRaises(SystemExit) as cm:
            controller.showMainMenu()
        self.assertEqual(cm.exception.code, 0)

        pass

    @patch("builtins.input", side_effect=['1', 'q'])
    # ['1', 'q', '5']: Show all tickets (1) through menu then quit (q).
    def test_show_all(self, input):
        controller = AppController()
        with self.assertRaises(SystemExit) as cm:
            controller.showMainMenu()
        self.assertEqual(cm.exception.code, 0)

        pass

    @patch("builtins.input", side_effect=['2', '3', '4'])  # shows ticket with ID 2, 3, 4
    def test_show_one(self, input):
        controller = AppController()
        self.assertEqual(controller.showOneTicket(), 0)
        self.assertEqual(controller.currID, 2)
        self.assertEqual(controller.showOneTicket(), 0)
        self.assertEqual(controller.currID, 3)
        self.assertEqual(controller.showOneTicket(), 0)
        self.assertEqual(controller.currID, 4)

        pass


if __name__ == "__main__":
    unittest.main()
    # TO-DO: report coverage after tests finish running.
