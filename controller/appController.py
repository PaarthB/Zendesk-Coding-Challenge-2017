"""
Controller package for the MVC pattern. Responsible for user I/O, drives the view logic and updates model state. Gets
data from model by querying it, and sends it to view to be displayed.
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

    def run(self):
        while True:
            self.showMainMenu()

    def getInput(self):
        self.input = input()
        return self.input

    def showMainMenu(self):
        while True:
            self.view.printMenu()

            if self.getInput() == '1':
                self.showAllTickets()

            elif self.getInput() == '2':
                a = self.showOneTicket()
                return a
            elif self.getInput() == 'q':
                print("Quit")
                self.view.quit()
            else:
                self.view.inputError()
                return 0
            self.input = ""

    def showWelcomeMenu(self):
        self.view.startMessage()
        while True:
            # self.getInput()
            if self.getInput() == "menu":
                self.showMainMenu()
            elif self.getInput() == "q":
                self.view.quit()
            else:
                self.view.inputError()
            self.input = ""

    def showAllTickets(self):
        try:
            tickets = self.api.getAllTickets()
        except RuntimeError:
            print("Couldn't fetch tickets. Error connecting to API or loading data from it")
            return None
        page = self.view.displayTickets(tickets, 1)
        while True:

            if self.getInput() == 'q':
                self.view.quit()
                break

            if self.getInput() == "menu":
                self.view.printMenu()
                break

            if self.getInput() == "d":
                page += 1
                page = self.view.displayTickets(tickets, page)

            if self.getInput() == "u":
                page -= 1
                page = self.view.displayTickets(tickets, page)
            else:
                self.view.inputError()
            self.input = ""
        return 0

    def showOneTicket(self):
        self.view.getTicketID()
        id = self.getInput()
        self.input = ""
        try:
            ticket = self.api.getTicketByID(id)
        except RuntimeError:
            print("Non-existent ticket ID. Can't fetch details. Please enter a valid ticket ID.")
            return None

        self.view.displaySingleTicket(ticket)
        self.currID = int(id)
        return 0


if __name__ == "__main__":
    t = AppController()
    t.run()
