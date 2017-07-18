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
        self.view = AppView()
        self.api = APIRequestHandler()
        self.input = ""
        self.currID = 999  # A random ticket ID. This points to the ticket we are currently viewing.
        self.currPage = 999  # A random page number. This points to the current page we are viewing.

    def run(self):
        self.showMainMenu()

    def getInput(self):
        self.input = input()

    def showMainMenu(self):
        self.view.startMessage()
        while True:
            self.getInput()
            if self.input == "menu":
                self.view.printMenu()
            elif self.input == '1':
                response = self.showAllTickets()
                if response is None: self.view.printMenu()
            elif self.input == '2':
                self.showOneTicket()
                self.view.printMenu()
            elif self.input == 'q':
                print("Quit")
                self.view.quit()
            else:
                self.view.inputError()
            self.input = ""

    def showAllTickets(self):
        try:
            tickets = self.api.getAllTickets()
            assert tickets not in [-1, 0, 1]
            page = self.view.displayTickets(tickets, 1)
        except AssertionError as e:
            if tickets == -1:
                self.view.unknownError()
            elif tickets == 1:
                self.view.authenticationError()
            elif tickets == 0:
                self.view.apiUnavailable()
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
                self.view.inputError()
            self.input = ""
            self.currPage = page
        return 0

    def showOneTicket(self):
        self.view.getTicketID()
        self.getInput()
        ticketID = self.input
        self.input = ""
        try:
            ticket = self.api.getTicketByID(ticketID)
            assert ticket not in [-1, 0, 1]
            self.view.displaySingleTicket(ticket, ticketID)
            self.currID = int(ticketID)
            return 0
        except AssertionError as e:
            if ticket == 1:
                self.view.authenticationError()
            elif ticket == -1:
                self.view.ticketIDError()
            elif ticket == 0:
                self.view.apiUnavailable()
            return False


if __name__ == "__main__":
    t = AppController()
    t.run()
