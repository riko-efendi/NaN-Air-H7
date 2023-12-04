class Employee:
    def __init__(self, name, kennitala, address, phone_number, email):
        self.name = name
        self.kennitala = kennitala
        self.address = address
        self.phone_number = phone_number
        self.email = email

class Pilot(Employee):
    def __init__(self, rank="Co-Pilot"):
        super().__init__()
        self.rank = rank

class CabinCrew(Employee):
    def __init__(self):
        super().__init__()
