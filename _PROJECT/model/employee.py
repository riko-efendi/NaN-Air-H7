class Employee:
    def __init__(self, kennitala:int=0, name:str="", role:str="", address:str="", phone_number:int=0, email:str=""):
        self.kennitala = kennitala
        self.name = name
        self.role = role
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def __str__(self) -> str:
        return f"{self.name}: {self.role}"

class Pilot(Employee):
    def __init__(self, rank="Co-Pilot"):
        super().__init__()
        self.rank = rank

class CabinCrew(Employee):
    def __init__(self):
        super().__init__()
