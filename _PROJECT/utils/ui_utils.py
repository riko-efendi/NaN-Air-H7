from model.employee import Employee
from model.destination import Destination

import os

class UIUtils:
    
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