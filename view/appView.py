"""
A static View in the view package for the MVC pattern. This view is controlled by the controller. 
Displays program messages and ticket information on the CLI screen
"""
import sys
import math


class AppView:
    def __init__(self):
        self.page_limit = 25
        self.errorCode = None
        self.messageType = ""
        self.badRequests = ["The ticket ID you gave is not a valid ID", "API unavailable. Please try again later",
                            "Either no tickets on account or unknown error occurred",
                            "API authentication not permitted or invalid user credentials."]
        self.programErrors = ["Invalid input entered. Please enter input again: ",
                              "Page command error. 'd' to go down, 'u' to go up, 'menu' for menu and 'q' for quit: "]

    def startMessage(self):
        print("\n\n-------------------WELCOME TO ZENDESK TICKET VIEWER---------------------")
        print("This application lets you view tickets and their details on your zendesk account")
        print("Please enter a command, to view command options, type 'menu': ", end="")
        return 0

    def displayErrorMessage(self, messageID):
        self.messageType = messageID
        self.printErrorMessage()
        return 1

    def printMenu(self):
        print("Menu Options:")
        print("1 : ", "Display all tickets")
        print("2 : ", "Display Single ticket")
        print("q : ", "Quit program")
        print("Enter your choice: ", end="")
        return 0

    def quit(self):
        print("Exiting Zendesk Ticket Viewer. . . . . .")
        print("Exiting successful, see you soon.")
        sys.exit(0)

    def fetchTickets(self, ticketID):
        if ticketID == "all":
            print("Fetching tickets, please wait . . . . .")
        else:
            print("Fetching ticket", ticketID + ",", "please wait . . . . .")
        return 0

    def getTicketID(self):
        print("Enter the ticket ID: ", end="")
        return 0

    def printErrorMessage(self):
        if self.messageType in [0, 1, 2, 3]:
            if self.errorCode is not None:
                print("Bad request. Error getting data from API. Error Code: ", self.errorCode)
            print(self.badRequests[int(self.messageType)])
        elif self.messageType in [4, 5]:
            print(self.programErrors[int(self.messageType) - 4], end="")

    def displayTickets(self, ticketsJSON, pageNo):
        ticketsArr = ticketsJSON["tickets"]
        # rounding up ticket pages
        totalPages = math.ceil(float(len(ticketsArr)) / float(self.page_limit))
        # circular rotation of pages after limit or before start
        if pageNo > totalPages: pageNo = 1
        elif pageNo < 1: pageNo = totalPages
        pageTickets = 0
        ticketOffset = (pageNo - 1) * self.page_limit
        for i in range(int(ticketOffset), int(self.page_limit + ticketOffset)):
            if i < len(ticketsArr):
                if ticketsArr[i]["id"] is None:
                    continue
                else:
                    print("<" + ticketsArr[i]["status"] + ">", "Ticket", ticketsArr[i]["id"], "opened by",
                          ticketsArr[i]["requester_id"], "updated at", ticketsArr[i]["updated_at"])
                pageTickets += 1
        print("Displaying", pageTickets, "tickets on page", pageNo, "of", totalPages)
        print("Enter 'd' to go down, 'u' to go up, 'menu' for menu and 'q' for quit: ", end="")
        return pageNo  # Current page no

    def displayTicket(self, ticketsJSON):
        if "ticket" in ticketsJSON:
            print("<" + ticketsJSON["ticket"]["status"] + ">", "Ticket", ticketsJSON["ticket"]["id"], "subject '",
                  ticketsJSON["ticket"]["subject"], "opened by", ticketsJSON["ticket"]["requester_id"], "updated at",
                  ticketsJSON["ticket"]["updated_at"])
            return 0
        else:
            return 1