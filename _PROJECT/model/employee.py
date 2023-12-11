"""
Employee base class. Here we give the employee all its variables.
"""

class Employee:

    def __init__(self, kennitala:int=0, name:str="", role:str="", rank:str="", address:str="", phone_number:int=0, email:str="", license:str=""):
        self.kennitala = kennitala
        self.print_kennitala = kennitala#[:6] + "-" + kennitala[6:]
        self.name = name
        self.role = role
        self.rank = rank
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.license = license

    # def __str__(self) -> str:
    #     return f"{self.name}: {self.role}"
