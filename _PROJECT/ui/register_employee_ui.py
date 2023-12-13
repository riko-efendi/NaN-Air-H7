from model.employee import Employee
from data.data_wrapper import DataWrapper
from utils.ui_utils import UIUtils
from ui.input_validation import *

class RegisterEmployeeUI():
    def __init__(self, data_connection:DataWrapper) -> None:
        self.logic_wrapper = data_connection
        self.ui_utils = UIUtils()

    def register_employee(self, employee:Employee, header:str):
        """Registers an employee"""
        
        self.ui_utils.print_employee(employee, header)
        #so the first check is for them to enter a valid name
        #name must contain only letters and have a set length for them as well
        while True:
            try:
                employee.name = input(f"Input the {employee.role}'s name: ").capitalize()
                validate_name(employee.name)
                self.ui_utils.print_employee(employee, header)
                break
            
            except LengthERROR:
                self.ui_utils.clear_screen()
                self.ui_utils.print_employee(employee, header)
                print("Name is out of range, please enter a valid length")
            
            except ValueError:
                self.ui_utils.clear_screen()
                self.ui_utils.print_employee(employee, header)
                print("Invalid name, please only use letters")

        #this checks the kennitala if the user inputs the right numbers for a kennitala and nothing random. 
        while True:
            try: 
                employee.kennitala = (input(f"Input the {employee.role}'s kennitala: "))
                validate_kennitala(employee.kennitala)
                self.ui_utils.print_employee(employee, header)
                break
            
            except LengthERROR:
                self.ui_utils.clear_screen()
                self.ui_utils.print_employee(employee, header)
                print("Invalid length, please enter a valid kennitala")
            except ValueError:
                self.ui_utils.clear_screen()
                self.ui_utils.print_employee(employee, header)
                print("invalid value, please enter a valid kennitala")

        #this checks the address. the validation of the address is that
        # first must contain a name for the adress and the 1 or 2 numbers for the number of that address 
        while True:
            try:
                employee.address = input(f"Input the {employee.role}'s address: ").capitalize()
                validate_address(employee.address)
                self.ui_utils.print_employee(employee, header)
                break

            except ValueError:
                self.ui_utils.clear_screen()
                self.ui_utils.print_employee(employee, header)
                print('Invalid address, please use format "streetname streetnumber"')
        
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
        #finally this checks the phone number if its valid numbers and length
        #instead of something random that the user inputs.
        while True: 
            try:
                employee.phone_number = input(f"Input the {employee.role}'s phone number: ")
                validate_phone_number(employee.phone_number)
                self.ui_utils.print_employee(employee, header)
                break
            
            except ValueError:
                self.ui_utils.clear_screen()
                self.ui_utils.print_employee(employee, header)
                print("Invalid value, please enter a valid phone number")
            except LengthERROR:
                self.ui_utils.clear_screen()
                self.ui_utils.print_employee(employee, header)
                print("Please inpout a valid phone number")
            
        self.logic_wrapper.register_employee(employee)
        input(f"{employee.name} is successfully created! Press [ENTER] to exit: ")
