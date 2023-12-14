from model.employee import Employee
from model.voyage import Voyage
from model.destination import Destination
from logic.logic_wrapper import LogicWrapper
import os

class UIUtils:
    
    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()

    def clear_screen(self):
        os_name = os.name.lower()
        if os_name == 'posix':  # Unix/Linux/MacOS
            os.system("clear")
        elif os_name == 'nt':   # Windows
            os.system("cls")

    def print_employee(self, employee:Employee, header:str=""):
        """Prints out a table of information on an Employee"""

        self.clear_screen()
        print(header + "\n")
        print(f"Name: {employee.name}")
        print(f"Kt: {employee.kennitala}")
        print(f"Address: {employee.address}")
        print(f"Role: {employee.role}")
        print(f"Rank: {employee.rank}")
        print(f"Phone number: {employee.phone_number}")
        print()

    def print_destination(self, destination:Destination, header:str="[REGISTER DESTINATION]"):
        """prints out a table of information of the destination"""
    
        self.clear_screen()
        print(header + "\n")
        print(f"Destination ID: {destination.id}")
        print(f"Destination: {destination.destination}")
        print(f"Numeric ID: {destination.numeric_id}")
        print(f"Flight time: {destination.flight_time_from_kef}")
        print()

    def print_voyages(self, voyages:Voyage, header:str=""):
        """Prints voyages and their crews"""

        self.clear_screen()
        print(f"{header}\n")

        for i, voyage in enumerate(voyages):

            # Check how many flight attendants are in the voyage
            fa_amount = []
            for key, value in voyage.flight_1.crew.items():
                if value != "" and key.startswith("fa"):
                    fa_amount.append(key)


            captain = self.logic_wrapper.get_employee_by_nid(voyage.flight_1.crew['captain'])
            captain = captain.name if captain != None else "No Crew Assigned"
            copilot = self.logic_wrapper.get_employee_by_nid(voyage.flight_1.crew['copilot'])
            copilot = copilot.name if copilot != None else "No Crew Assigned"
            fsm = self.logic_wrapper.get_employee_by_nid(voyage.flight_1.crew['fsm'])
            fsm = fsm.name if fsm != None else "No Crew Assigned"

            print(f"{i + 1}. Voyage id:[{voyage.id}]")
            print(f"\tGoing a round trip from {voyage.flight_1.dep_from} to {voyage.flight_1.arr_at}.")
            print(f"\t[{voyage.depart_date}] - [{voyage.arr_date}]")
            print(f"\tCaptain:                {captain}")
            print(f"\tCopilot:                {copilot}")
            print(f"\tFlight Service Manager: {fsm}")

            # Iterate through the flight attendants
            for k, fa in enumerate(fa_amount):
                try:
                    flight_attendant = self.logic_wrapper.get_employee_by_nid(voyage.flight_1.crew[fa])
                    print(f"\tFlight Attendant {k + 1}:     {flight_attendant.name}")
                except AttributeError:
                    print(f"\tFlight Attendant {k + 1}:     Employee no longer registered")

            print()
