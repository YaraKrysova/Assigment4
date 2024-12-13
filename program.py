import json
import csv
from datetime import datetime

def log_action(action):
    with open("ProgramLog.txt", "a") as log_file:
        log_file.write(f"{datetime.now()} - {action}\n")

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
    def __init__(self):
        self._letters = []



    def openLetterData(self):
        try:
            with open("Letters.json", "r") as file:
                data = json.load(file)
                self._letters = [Letter(**entry) for entry in data]
                log_action("Opened letter data")
                
        except Exception as e:
            print(f"Error reading file: {e}")


    def saveLetterData(self):
        try:
            with open("Letters.json", "w") as file:
                json.dump([letter.getJson() for letter in self._letters], file, indent=4)
                log_action("Saved letter data")

        except Exception as e:
            print(f"Error saving letter data: {e}")



    def importChildrenData(self):
        try:
            with open("ChildrenList.csv", "r") as file:
                for row in file:
                    letter = next((l for l in self._letters if l._id == int(row["Letter ID"])), None)
                    if letter:
                        letter.getApproval(row["Nice"].strip().lower() == "true")
            self.saveLetterData()
            log_action("Imported children data")
        except Exception as e:
            print(f"HO-HO-HO *Santa Claus noises*, seems like this kid doesn't exist")


    def exportToyManufacturingData(self):
        try:
            with open("RequestedToys.csv", "w", newline="") as file:
                fieldNames = ["Name", "Category", "Description"]
                writer = csv.DictWriter(file, fieldNames=fieldNames)
                writer.writeheader()
                for letter in self._letters:
                    for toy in letter.getToys():
                        writer.writerow(toy)
                log_action("Exported toy manufacturing data")
        except Exception as e:
            print(f"Error exporting toy manufacturing data: {e}")
