from model.employee import Employee
from data.data_wrapper import DataWrapper
from utils.ui_utils import UIUtils
from ui.input_validation import LengthError, validate_length, validate_length_kt, validate_integers, validate_letters,validate_length_phone, validate_address

class RegisterEmployeeUI():
    def __init__(self, data_connection:DataWrapper) -> None:
        self.logic_wrapper = data_connection
        self.ui_utils = UIUtils()

    def register_employee(self, employee:Employee, header:str):
        """Registers an employee"""
        
        self.ui_utils.print_employee(employee, header)
        while True:
            try:
                employee.name = input(f"Input the {employee.role}'s name: ").capitalize()
                validate_length(employee.name)
                validate_letters(employee.name)
                self.ui_utils.print_employee(employee, header)
                break
            
            except LengthError:
                print("Name is out of range, please enter a valid length")
            
            except ValueError:
                print("Invalid name, please only use letters")


        while True:
            try: 
                employee.kennitala = (input(f"Input the {employee.role}'s kennitala: "))
                validate_integers(employee.kennitala)
                validate_length_kt(employee.kennitala)
                self.ui_utils.print_employee(employee, header)
                break
            
            except LengthError:
                print("Invalid length, please enter a valid kennitala")

            except ValueError:
                print("invalid value, please enter a valid kennitala")

        
        while True:
            try:
                employee.address = input(f"Input the {employee.role}'s address: ").capitalize()
                validate_address(employee.address)
                self.ui_utils.print_employee(employee, header)
                break

            except ValueError:
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
        while True: 
            try:
                employee.phone_number = input(f"Input the {employee.role}'s phone number: ")
                validate_integers(employee.phone_number)
                validate_length_phone(employee.phone_number)
                self.ui_utils.print_employee(employee, header)
                break
            
            except ValueError:
                print("Invalid value, please enter a valid phone number")

            except LengthError:
                print("Please inpout a valid phone number")
            
            
        self.logic_wrapper.register_employee(employee)
        
        input(f"{employee.name} is successfully created! Press [ENTER] to exit: ")
