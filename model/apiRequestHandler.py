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
        multiple = True
        ticketsJSON = self.connectToAPI(True, "")
        # print(ticketsJSON)
        ticketsJSON = self.formatJSON(ticketsJSON, False)
        return ticketsJSON

    def getTicketByID(self, ticketID):
        print("Fetching ticket ", ticketID, ", please wait . . . . .")
        ticketsJSON = self.connectToAPI(False, ticketID)
        # print(ticketsJSON)
        ticketsJSON = self.formatJSON(ticketsJSON, True)
        return ticketsJSON

    def connectToAPI(self, all=True, id=""):
        subdomain = "paarth"
        loginID = "paarthbhasin4@gmail.com"
        password = "Adprs123!"

        if all:
            self.URL = "https://" + subdomain + ".zendesk.com/api/v2/tickets.json"
        else:
            self.URL = "https://" + subdomain + ".zendesk.com/api/v2/tickets/" + id + ".json"
        try:
            r = requests.get(self.URL, auth=(loginID, password))
            self.data = json.loads(r.text)
            return self.data
        except requests.exceptions.HTTPError as e:
            print(e)
            print("Invalid user credentials, can't authorize you.")
            return None
        except requests.exceptions.RequestException as e:
            print(e)
            print("Error connecting to the API due to unavailability")
            return None

    def formatJSON(self, ticketsJSON, single=False):
        if single:
            t1 = time.strptime(ticketsJSON["ticket"]["updated_at"], "%Y-%m-%dT%H:%M:%SZ")
            t2 = time.strptime(ticketsJSON["ticket"]["created_at"], "%Y-%m-%dT%H:%M:%SZ")
            updated = "%d-%d-%d %d:%d:%d" % (t1[0], t1[1], t1[2], t1[3], t1[4], t1[5])
            created = "%d-%d-%d %d:%d:%d" % (t2[0], t2[1], t2[2], t2[3], t2[4], t2[5])
            ticketsJSON["ticket"]["updated_at"] = updated
            ticketsJSON["ticket"]["created_at"] = created
            return ticketsJSON
        else:
            tickets = ticketsJSON["tickets"]
            for i in range(len(tickets)):
                t1 = time.strptime(ticketsJSON["tickets"][i]["updated_at"], "%Y-%m-%dT%H:%M:%SZ")
                t2 = time.strptime(ticketsJSON["tickets"][i]["created_at"], "%Y-%m-%dT%H:%M:%SZ")
                updated = "%d-%d-%d %d:%d:%d" % (t1[0], t1[1], t1[2], t1[3], t1[4], t1[5])
                created = "%d-%d-%d %d:%d:%d" % (t2[0], t2[1], t2[2], t2[3], t2[4], t2[5])
                ticketsJSON["tickets"][i]["updated_at"] = updated
                ticketsJSON["tickets"][i]["created_at"] = created
            return ticketsJSON
