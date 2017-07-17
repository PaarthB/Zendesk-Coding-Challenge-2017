"""
Model of the model package in MVC pattern. Does all the API stuff: authentication, fetching tickets, processing data got 
from the API.
It can be extended in the future to extra functionality like posting new data up on the server, token authentication.
"""
import requests
import datetime


class APIRequestHandler:
    def __init__(self):
        self.URL = ""
        self.data = {}

    def getAllTickets(self):
        ticketsJSON = self.connectToAPI(True, "")
        if ticketsJSON not in [False, None] and "tickets" in ticketsJSON:
            print("Total tickets= ", len(ticketsJSON["tickets"]))
            for i in range(len(ticketsJSON["tickets"])):
                updated, created = self.formatDates(ticketsJSON["tickets"][i]["updated_at"],
                                                    ticketsJSON["tickets"][i]["created_at"])
                ticketsJSON["tickets"][i]["updated_at"] = str(updated)  # Setting the formatted dates
                ticketsJSON["tickets"][i]["created_at"] = str(created)  # Setting the formatted dates
            return ticketsJSON
        elif not ticketsJSON or ticketsJSON is None:
            return 0

    def getTicketByID(self, ticketID):
        print("Fetching ticket ", ticketID, ", please wait . . . . .")
        ticketsJSON = self.connectToAPI(False, ticketID)
        if ticketsJSON not in [None, False] and 'ticket' in ticketsJSON:
            updated, created = self.formatDates(ticketsJSON["ticket"]["updated_at"],
                                                ticketsJSON["ticket"]["created_at"])
            ticketsJSON["ticket"]["updated_at"] = str(updated)
            ticketsJSON["ticket"]["created_at"] = str(created)
            return ticketsJSON
        elif not ticketsJSON or ticketsJSON is None:
            return 0
        return 1

    def connectToAPI(self, all=True, id=""):
        subdomain = "paarth"
        loginID = "paarthbhasin4@gmail.com"
        password = "Adprs123!"

        if all:
            self.URL = "https://" + subdomain + ".zendesk.com/api/v2/tickets.json"
        else:
            self.URL = "https://" + subdomain + ".zendesk.com/api/v2/tickets/" + str(id) + ".json"
        try:
            r = requests.get(self.URL, auth=(loginID, password))
            if r.status_code != 200:
                print("Bad request. Error getting data from API. Error Code: ", r.status_code)
                return False
            self.data = r.json()  # Or json.loads(r.text) can also work
            new = self.data
            next_page = []
            # Go through all web pages containing tickets and add them to tickets json. One page can contain 100 tickets
            # Make sure user has chosen to display all tickets, next page exists and has not been already visited.
            while all and new["next_page"] is not None and new["next_page"] not in next_page:
                self.URL = new["next_page"]
                next_page.append(self.URL)
                # print(self.URL)
                r = requests.get(self.URL, auth=(loginID, password))
                new = r.json()
                print("Next: ", new["next_page"])
                self.data["tickets"].extend(new["tickets"])  # Adding new tickets found in the next API web page.

            return self.data
        except requests.exceptions.HTTPError as e:
            print(e)
            print("Can't authorize you, invalid credentials. ")
            return None
        except requests.exceptions.RequestException as e:
            print(e)
            print("API unavailable. Please try again later")
            return None
        except ConnectionError:
            print("Connection Error.")
            return None

    def formatDates(self, updatedAt, createdAt):
        t1 = datetime.datetime.strptime(updatedAt, "%Y-%m-%dT%H:%M:%SZ")
        t2 = datetime.datetime.strptime(createdAt, "%Y-%m-%dT%H:%M:%SZ")
        updated = "%d-%d-%d %d:%d:%d" % (t1.year, t1.month, t1.day, t1.hour, t1.minute, t1.second)
        created = "%d-%d-%d %d:%d:%d" % (t2.year, t2.month, t2.day, t2.hour, t2.minute, t2.second)
        return updated, created
