"""
Controller of the controller package for the MVC pattern. Responsible for user I/O, drives the view logic and updates 
model state. Gets data from model by querying it, and sends it to view to be displayed.
"""
import sys
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))

from view.appView import AppView
from model.apiRequestHandler import APIRequestHandler


class AppController:
    def __init__(self):
        self.view = AppView()  # An AppView instance being used by this class
        self.api = APIRequestHandler()  # An APIRequestHandler instance being used by this class
        self.input = ""  # Input given by user
        self.currID = 999  # A random ticket ID. This points to the ticket we are currently viewing.
        self.currPage = 999  # A random page number. This points to the current page we are viewing.

    def run(self):  # Driver method
        self.showMainMenu()

    def getInput(self):  # Prompts user for input
        self.input = input()

    def showMainMenu(self):  # Main menu view controller
        self.view.startMessage()
        while True:
            self.getInput()
            if self.input == "menu":
                self.view.printMenu()
            elif self.input == '1':
                response = self.showTickets()
                if response is None: self.view.printMenu()
            elif self.input == '2':
                self.showTicket()
                self.view.printMenu()
            elif self.input == 'q':
                print("Quit")
                self.view.quit()
            else:
                self.view.displayErrorMessage(4)
            self.input = ""

    def showTickets(self):  # Controller method to display all tickets. Handles user inputs for paging requests
        try:
            self.view.fetchTickets("all")
            tickets = self.api.getTickets()
            assert tickets not in [-1, 0, 1]
            page = self.view.displayTickets(tickets, 1)
        except AssertionError as e:
            self.view.errorCode = self.api.errorCode
            if tickets == -1:
                self.view.displayErrorMessage(2)
            elif tickets == 1:
                self.view.displayErrorMessage(3)
            elif tickets == 0:
                self.view.displayErrorMessage(1)
            self.view.errorCode = None
            self.api.errorCode = None
            return None
        while True:
            self.getInput()
            if self.input == 'q':
                self.view.quit()
                break

            elif self.input == "menu":
                self.view.printMenu()
                break
            elif self.input == "d":
                page += 1
                page = self.view.displayTickets(tickets, page)

            elif self.input == "u":
                page -= 1
                page = self.view.displayTickets(tickets, page)
            else:
                self.view.displayErrorMessage(4)
            self.input = ""
            self.currPage = page
        return 0

    def showTicket(self):  # Controller method for displaying one ticket in view
        self.view.getTicketID()
        self.getInput()
        ticketID = self.input
        self.input = ""
        try:
            self.view.fetchTickets(ticketID)
            ticket = self.api.getTicket(ticketID)
            assert ticket not in [-1, 0, 1]
            self.view.displayTicket(ticket)
            self.currID = int(ticketID)
            return 0
        except AssertionError as e:
            self.view.errorCode = self.api.errorCode
            if ticket == 1:
                self.view.displayErrorMessage(3)
            elif ticket == -1:
                self.view.displayErrorMessage(0)
            elif ticket == 0:
                self.view.displayErrorMessage(1)
            self.view.errorCode = None
            self.api.errorCode = None
            return False


if __name__ == "__main__":
    t = AppController()  # Starting point of the application
    t.run()
