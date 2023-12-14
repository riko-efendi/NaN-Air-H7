from model.employee import Employee
from model.voyage import Voyage
from logic.logic_wrapper import LogicWrapper
import os

DASH_AMOUNT = 46

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
        dash = (DASH_AMOUNT - len(header))
        self.clear_screen()
        print(header + (dash * "-"))
        print("\n" * 4)
        print(f"Name: {employee.name}")
        print(f"Kt: {employee.kennitala}")
        print(f"Address: {employee.address}")
        print(f"Role: {employee.role}")
        print(f"Rank: {employee.rank}")
        print(f"Phone number: {employee.phone_number}")
        print()


    def print_voyages(self, voyages:Voyage, header:str=""):
        """Prints voyages and their crews"""
        self.clear_screen()
        print("-" * DASH_AMOUNT)
        print(f"{header:^46}") 
        print("-" * DASH_AMOUNT + "\n")

        for index, voyage in enumerate(voyages):
            captain = self.logic_wrapper.get_employee_by_nid(voyage.flight_1.captain)
            captain = captain.name if captain != None else "No Crew Assigned"
            copilot = self.logic_wrapper.get_employee_by_nid(voyage.flight_1.copilot)
            copilot = copilot.name if copilot != None else "No Crew Assigned"
            fsm = self.logic_wrapper.get_employee_by_nid(voyage.flight_1.fsm)
            fsm = fsm.name if fsm != None else "No Crew Assigned"
            fa1 = self.logic_wrapper.get_employee_by_nid(voyage.flight_1.fa1)
            fa1 = fa1.name if fa1 != None else "No Crew Assigned"
            fa2 = self.logic_wrapper.get_employee_by_nid(voyage.flight_1.fa2)
            fa2 = fa2.name if fa2 != None else "No Crew Assigned"

            
            print(f"{index + 1}. Voyage id:[{voyage.id}]")
            print(f"\tGoing a round trip from {voyage.flight_1.dep_from} to {voyage.flight_1.arr_at}.")
            print(f"\t[{voyage.depart_date}] - [{voyage.arr_date}]")
            print(f"\tCaptain:                {captain}")
            print(f"\tCopilot:                {copilot}")
            print(f"\tFlight Service Manager: {fsm}")
            print(f"\tFlight Attendant 1:     {fa1}")
            print(f"\tFlight Attendant 2:     {fa2}")
            print()