"""
Employee base class. Here we give the employee all its variables.
"""

class Employee:

    def __init__(self, kennitala:str="", name:str="", role:str="", rank:str="", address:str="", phone_number:str="", license:str=""):
        self.kennitala = kennitala
        self.print_kennitala = kennitala
        self.name = name
        self.role = role
        self.rank = rank
        self.address = address
        self.phone_number = phone_number
        self.license = license


