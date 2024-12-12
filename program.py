import json


class Toy:
    def __init__(self, name, category, description):
        self._name = name
        self._category = category
        self._description = description

    def turnIntoDict(self):     #this method returns info as dictionary
        return {
            "Name": self._name,
            "Category": self._category,
            "Description": self._description
        }

class Letter:
    def __init__(self, id, firstName, lastName, toys, approved = None):
        self._id = id
        self._firstName = firstName
        self._lastName = lastName
        self._toys = [Toy(**toy) for toy in toys] #list of dictionaries
        self._approved = approved

    def childDict(self):
        return {
            "Letter ID": self._id,
            "Full Name": f"{self._firstName} {self._lastName}",
            "Nice": ""
        }
    
    def getApproval(self, approvalStatus):
        self._approved = approvalStatus

    def getJson(self):
        return {
            "id": self._id,
            "first_name": self._firstName,
            "last_name": self._lastName,
            "toys": [toy.turnIntoDict() for toy in self._toys],
            "approved": self._approved
        }       #returning a dictionary representation of its attribute
    
    def getToys(self):
        return [toy.turnIntoDict() for toy in self._toys]

class Program:
    pass




