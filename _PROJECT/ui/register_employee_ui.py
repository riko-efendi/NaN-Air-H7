from model.employee import Employee
from data.data_wrapper import DataWrapper
from utils.ui_utils import UIUtils
from ui.input_validation import LengthError, validate_length, validate_length_kt, validate_integers, validate_letters,validate_length_phone, validate_address

import time
DASH_AMOUNT = 46

class RegisterEmployeeUI():
    def __init__(self, data_connection:DataWrapper) -> None:
        self.logic_wrapper = data_connection
        self.ui_utils = UIUtils()

    def register_employee(self, employee:Employee, header:str):
        """Registers an employee"""
        self.ui_utils.print_employee(employee, header)
        print("\n" * 3)
        print("-" * DASH_AMOUNT + "\n")
        user_input = input(f"Input the {employee.role}'s name: ").capitalize()
        while True:
            try:
                validate_length(user_input)
                validate_letters(user_input)
                employee.name = user_input
                self.ui_utils.print_employee(employee, header)
                break
            
            except LengthError:
                self.ui_utils.print_employee(employee, header)
                print("\n" * 3)
                print("-" * DASH_AMOUNT + "\n")
                user_input = input("\033[31mName is out of range\033[0m, please enter a valid length: ")
                time.sleep(1.5)
            
            except ValueError:
                self.ui_utils.print_employee(employee, header)
                print("\n" * 3)
                print("-" * DASH_AMOUNT + "\n")
                user_input = input("\033[31mInvalid Value\033[0m, please only use letters: ")
                


        print("\n" * 3)
        print("-" * DASH_AMOUNT + "\n")
        user_input = (input(f"Input the {employee.role}'s kennitala: "))
        while True:
            try: 
                validate_integers(user_input)
                validate_length_kt(user_input)
                employee.kennitala = user_input
                self.ui_utils.print_employee(employee, header)
                break
            
            except LengthError:
                self.ui_utils.print_employee(employee, header)
                print("\n" * 3)
                print("-" * DASH_AMOUNT + "\n")
                user_input = input("\033[31mInvalid Length\033[0m, please enter a valid kennitala: ")

            except ValueError:
                self.ui_utils.print_employee(employee, header)
                print("\n" * 3)
                print("-" * DASH_AMOUNT + "\n")
                user_input = input("\033[31mInvalid Value\033[0m, please enter a valid kennitala: ")


        print("\n" * 3)
        print("-" * DASH_AMOUNT + "\n")
        user_input = input(f"Input the {employee.role}'s address: ").capitalize()
        while True:
            try:
                validate_address(user_input)
                employee.address = user_input
                self.ui_utils.print_employee(employee, header)
                break

            except ValueError:
                self.ui_utils.print_employee(employee, header)
                print("\n" * 3)
                print("-" * DASH_AMOUNT + "\n")
                user_input = input('\033[31mInvalid address.\033[0m Please use format "StreetName StreetNumber: "')
                time.sleep(1.5)
        
        print("\n" * 3)
        print("-" * DASH_AMOUNT + "\n")
        if employee.role == "Pilot":
            e_rank = input(f"Is the {employee.role}: \n1. Captain\n2. Copilot\nEnter your choice: ")
            while e_rank != "1" and e_rank != "2":
                e_rank = input(f"Is the {employee.role}'s: \n1. Captain\n2. Copilot\n\033[31mInvalid.\033[0m Choose either 1 or 2: ")
            if e_rank == "1":
                employee.rank = "Captain"
            elif e_rank == "2":
                employee.rank = "Copilot"
        else:
            e_rank = input(f"Is the {employee.role}: \n1. Flight Service Manager\n2. Flight Attendant\nEnter your choice: ")
            while e_rank != "1" and e_rank != "2":
                e_rank = input(f"Is the {employee.role}: \n1. Flight Service Manager\n2. Flight Attendant\n\033[31mInvalid.\033[0m Choose either 1 or 2: ")
            if e_rank == "1":
                employee.rank = "Flight Service Manager"
            elif e_rank == "2":
                employee.rank = "Flight Attendant"
                
        self.ui_utils.print_employee(employee, header)
        print("\n" * 3)
        print("-" * DASH_AMOUNT + "\n")
        user_input =  input(f"Input the {employee.role}'s phone number: ")
        while True: 
            try:
                validate_integers(user_input)
                validate_length_phone(user_input)
                employee.phone_number = user_input
                self.ui_utils.print_employee(employee, header)
                break
            
            except ValueError:
                self.ui_utils.print_employee(employee, header)
                print("\n" * 3)
                print("-" * DASH_AMOUNT + "\n")
                user_input = input("\033[31mInvalid Value.\033[0m Please use 7 digits phone number: ")

            except LengthError:
                self.ui_utils.print_employee(employee, header)
                print("\n" * 3)
                print("-" * DASH_AMOUNT + "\n")
                user_input = input("\033[31mInvalid Length.\033[0m Please input 7 digits phone number: ")
            
            
        self.logic_wrapper.register_employee(employee)
        print("\n" * 3)
        print("-" * DASH_AMOUNT + "\n")
        input(f"{employee.name} is successfully registered! \nPress \033[34m[ENTER]\033[0m to exit: ")
