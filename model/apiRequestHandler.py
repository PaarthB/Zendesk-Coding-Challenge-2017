"""
Model of the model package in MVC pattern. Does all the API stuff: authentication, fetching tickets, processing data got 
from the API.
It can be extended in the future to extra functionality like posting new data up on the server, token authentication.
"""
import json
import requests
import time


class APIRequestHandler:
    def __init__(self):
        self.URL = ""
        self.data = {}

    def getAllTickets(self):
        ticketsJSON = self.connectToAPI(True, "")
        if "tickets" in ticketsJSON:
            for i in range(len(ticketsJSON)):
                updated, created = self.formatDates(ticketsJSON["tickets"][i]["updated_at"],
                                                    ticketsJSON["tickets"][i]["created_at"])
                ticketsJSON["tickets"][i]["updated_at"] = str(updated)
                ticketsJSON["tickets"][i]["created_at"] = str(created)

            return ticketsJSON
        else:
            return 0

    def getTicketByID(self, ticketID):
        print("Fetching ticket ", ticketID, ", please wait . . . . .")
        ticketsJSON = self.connectToAPI(False, ticketID)
        if "ticket" in ticketsJSON:
            updated, created = self.formatDates(ticketsJSON["ticket"]["updated_at"],
                                                ticketsJSON["ticket"]["created_at"])
            ticketsJSON["ticket"]["updated_at"] = str(updated)
            ticketsJSON["ticket"]["created_at"] = str(created)
            return ticketsJSON
        else:
            return 0

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
            return self.data
        except requests.exceptions.HTTPError as e:
            print(e)
            print("Invalid user credentials, can't authorize you.")
            return None
        except requests.exceptions.RequestException as e:
            print(e)
            print("Error connecting to the API due to unavailability")
            return None
        except ConnectionError:
            print("Connection Error.")
            return None

    def formatDates(self, updatedAt, createdAt):
        t1 = time.strptime(updatedAt, "%Y-%m-%dT%H:%M:%SZ")
        t2 = time.strptime(createdAt, "%Y-%m-%dT%H:%M:%SZ")
        updated = "%d-%d-%d %d:%d:%d" % (t1[0], t1[1], t1[2], t1[3], t1[4], t1[5])
        created = "%d-%d-%d %d:%d:%d" % (t2[0], t2[1], t2[2], t2[3], t2[4], t2[5])
        return updated, created
