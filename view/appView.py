"""
A static View in the view package for the MVC pattern. This view is controlled by the controller. 
Displays program messages and ticket information on the CLI screen
"""
import math


class AppView:
    def __init__(self):
        self.page_limit = 25
        self.errorCode = None
        self.badRequests = ["The ticket ID you gave is not a valid ID", "API unavailable. Please try again later",
                            "No tickets on account to display",
                            "API authentication not permitted or invalid user credentials.", "Unknown Bad Request"]
        self.programErrors = ["Invalid input, please enter input again. To view command menu type 'menu': ",
                              "Page command error. 'd' to go down, 'u' to go up, 'menu' for menu and 'q' for quit: "]

    def startMessage(self):  # Displays Start message on CLI screen
        print("\n\n-------------------------WELCOME TO ZENDESK TICKET VIEWER-------------------------")
        print("This application lets you view tickets and their details on your zendesk account")
        print("Please enter a command, to view command options, type 'menu': ", end="")
        return 0

    def displayErrorMessage(self, messageID):  # Displays error messages on CLI screen based on error message ID
        if messageID in [0, 1, 2, 3, 4]:
            if self.errorCode is not None:
                print("Bad request. Error getting data from API. Error Code:", self.errorCode)
            print(self.badRequests[int(messageID)])
        elif messageID in [5, 6]:
            print(self.programErrors[int(messageID) - 5], end="")
        return 1

    def printMenu(self):  # Displays Command Menu on CLI Screen
        print("Command Options:")
        print("1 :", "Display all tickets")
        print("2 :", "Display Single ticket")
        print("q :", "Exit application")
        print("menu : Display command menu")
        print("Enter your choice: ", end="")
        return 0

    def quit(self):  # Displays quit message and quits the App
        print("Exiting Zendesk Ticket Viewer. . . . . .")
        print("Exiting successful, see you soon.")
        return 0

    def fetchTickets(self, ticketID):  # Displays loading tickets message on CLI screen
        if ticketID == "all":
            print("Fetching tickets, please wait . . . . .")
        else:
            print("Fetching ticket", ticketID + ",", "please wait . . . . .")
        return 0

    def getTicketID(self):  # Displays input prompt message on CLI screen
        print("Enter the ticket ID: ", end="")
        return 0

    def displayTickets(self, ticketsJSON, pageNo):  # Displays tickets details with pagination on CLI screen
        ticketsArr = ticketsJSON["tickets"]
        # rounding up ticket pages
        totalPages = math.ceil(float(len(ticketsArr)) / float(self.page_limit))
        # circular rotation of pages after limit or before start
        if pageNo > totalPages:
            pageNo = 1
        elif pageNo < 1:
            pageNo = totalPages
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

    def displayTicket(self, ticketsJSON):  # Displays one ticket details on CLI screen
        if "ticket" in ticketsJSON:
            print("<" + ticketsJSON["ticket"]["status"] + ">", "Ticket", ticketsJSON["ticket"]["id"], "subject '",
                  ticketsJSON["ticket"]["subject"], "opened by", ticketsJSON["ticket"]["requester_id"], "updated at",
                  ticketsJSON["ticket"]["updated_at"])
            print("Please enter a command, to view command menu, type 'menu': ", end="")
            return 0
        else:
            return 1
