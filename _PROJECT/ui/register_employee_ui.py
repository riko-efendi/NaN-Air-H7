from model.employee import Employee
from data.data_wrapper import DataWrapper
from utils.ui_utils import UIUtils


class RegisterEmployeeUI():
    def __init__(self, data_connection:DataWrapper) -> None:
        self.logic_wrapper = data_connection
        self.ui_utils = UIUtils()

    def register_employee(self, employee:Employee, header:str):
        """Registers an employee"""
        
        self.ui_utils.print_employee(employee, header)
        employee.name = input(f"Input the {employee.role}'s name: ")
        self.ui_utils.print_employee(employee, header)
        employee.kennitala = (input(f"Input the {employee.role}'s kennitala: "))
        self.ui_utils.print_employee(employee, header)
        employee.address = input(f"Input the {employee.role}'s address: ").capitalize()
        self.ui_utils.print_employee(employee, header)

        if employee.role == "Pilot":
            e_rank = input(f"Is the {employee.role}: \n1. Captain\n2. Copilot\nEnter your choice: ")
            while e_rank != "1" and e_rank != "2":
                e_rank = input(f"Is the {employee.role}'s: \n1. Captain\n2. Copilot\nInvalid. Choose either 1 or 2: ")
            if e_rank == "1":
                employee.rank = "Captain"
            elif e_rank == "2":
                employee.rank = "Copilot"
        else:
            e_rank = input(f"Is the {employee.role}: \n1. Flight Service Manager\n2. Flight Attendant\nEnter your choice: ")
            while e_rank != "1" and e_rank != "2":
                e_rank = input(f"Is the {employee.role}: \n1. Flight Service Manager\n2. Flight Attendant\nInvalid. Choose either 1 or 2: ")
            if e_rank == "1":
                employee.rank = "Flight Service Manager"
            elif e_rank == "2":
                employee.rank = "Flight Attendant"
                
        self.ui_utils.print_employee(employee, header)
        employee.phone_number = input(f"Input the {employee.role}'s phone number: ")
        self.ui_utils.print_employee(employee, header)
        self.logic_wrapper.register_employee(employee)
        input(f"{employee.name} is successfully created! Press [ENTER] to exit: ")
