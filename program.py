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
    pass


class Program:
    pass




