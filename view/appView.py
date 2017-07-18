"""
A static View in the view package for the MVC pattern. This view is controlled by the controller and displays ticket 
information & general program related outputs to the CLI screen
"""
import sys
import math


class AppView:
    def __init__(self):
        self.page_limit = 25

    def startMessage(self):
        print("\n\n-------------------WELCOME TO ZENDESK TICKET VIEWER---------------------")
        print("This application lets you view tickets and their details on your zendesk account")
        print("Please enter a command, to view command options, type 'menu': ", end="")
        return 0

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

    def getTicketID(self):
        print("Enter the ticket ID: ", end="")
        return 0

    def inputError(self):
        print("Invalid input entered. Please enter input again: ", end="")
        return 1

    def ticketIDError(self):
        print("The ticket ID you gave is not a valid ID")
        return 1

    def pageCommandError(self):
        print("Page command error. Enter 'd' for down, 'u' for up, 'menu' for menu and 3 for quit")
        return 1

    def unknownError(self):
        print("Either no tickets on account or unknown error occurred")
        return 1

    def authenticationError(self):
        print("Authentication not permitted or invalid user credentials.")
        return 1

    def apiUnavailable(self):
        print("API unavailable. Please try again later")
        return 1

    def displayTickets(self, ticketsJSON, pageNo):
        ticketsArr = ticketsJSON["tickets"]
        # rounding up ticket pages
        totalPages = math.ceil(float(len(ticketsArr)) / float(self.page_limit))

        # circular rotation of pages after limit or before start
        if (pageNo > totalPages):
            pageNo = 1
        elif (pageNo < 1):
            pageNo = totalPages
        pageTickets = 0
        ticketOffset = (pageNo - 1) * self.page_limit
        for i in range(int(ticketOffset), int(self.page_limit + ticketOffset)):
            if i < len(ticketsArr):
                if ticketsArr[i]["id"] is None:
                    continue
                else:
                    self.printTicket(ticketsArr[i]["id"], ticketsArr[i]["status"], "",
                                     ticketsArr[i]["requester_id"], ticketsArr[i]["updated_at"])
                pageTickets += 1

        print("Displaying", pageTickets, "tickets on page", pageNo, "of", totalPages)
        print("Enter 'd' for next page, 'u' for previous page, 'menu' for menu and q for quit")
        return pageNo  # Current page no

    def displaySingleTicket(self, ticketsJSON, ticketID=""):
        print("Fetching ticket ", ticketID, ", please wait . . . . .")
        if "ticket" in ticketsJSON:
            self.printTicket(ticketsJSON["ticket"]["id"], ticketsJSON["ticket"]["status"],
                             ticketsJSON["ticket"]["subject"], ticketsJSON["ticket"]["requester_id"],
                             ticketsJSON["ticket"]["updated_at"])
            return 0
        else:
            return 1

    def printTicket(self, ticketID, status, subject="", requesterID="", updatedAt=""):
        if subject == "":
            print("<" + status + ">", "Ticket", str(ticketID), "opened by", requesterID,
                  "updated at", updatedAt)
        else:
            print("<" + status + ">", "Ticket", str(ticketID), "subject '" + subject + "'", "opened by", requesterID,
                  "updated at", updatedAt)

        return 0
