from model.employee import Employee
from data.data_wrapper import DataWrapper
from utils.ui_utils import UIUtils
from ui.input_validation import *



class RegisterEmployeeUI():
    def __init__(self, data_connection:DataWrapper) -> None:
        self.data_wrapper = data_connection
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
            
            except LengthError:
                self.ui_utils.print_employee(employee, header)
                print("\033[31mName is out of range\033[0m, please enter a valid length")
            
            except ValueError:
                self.ui_utils.print_employee(employee, header)
                print("\033[31mInvalid Value\033[0m, please only use letters")



        #this checks the kennitala if the user inputs the right numbers for a kennitala and nothing random. 
        while True:
            try: 
                employee.kennitala = (input(f"Input the {employee.role}'s kennitala: "))
                validate_kennitala(employee.kennitala)
                
                kennitala_list = []
                all_employees = self.data_wrapper.get_all_employees()
                for person in all_employees:
                    kennitala_list.append(person.kennitala)
                if employee.kennitala not in kennitala_list:
                    self.ui_utils.print_employee(employee, header)    
                    break
                else:
                    self.ui_utils.print_employee(employee, header)   
                    print("This kennlitala is \033[31malready assigned\033[0m to an existing employee.")

            except LengthError:
                self.ui_utils.print_employee(employee, header)
                print("\033[31mInvalid Length\033[0m, please enter a valid kennitala")
            except ValueError:
                self.ui_utils.print_employee(employee, header)
                print("\033[31mInvalid Value\033[0m, please enter a valid kennitala")

            
        #this checks the address. the validation of the address is that
        # first must contain a name for the adress and the 1 or 2 numbers for the number of that address 
        while True:
            try:
                employee.address = input(f"Input the {employee.role}'s address: ").capitalize()
                validate_address(employee.address)
                self.ui_utils.print_employee(employee, header)
                break

            except ValueError:
                self.ui_utils.print_employee(employee, header)
                print('\033[31mInvalid Value\033[0m. Please enter the right format"streetname streetnumber"')

            except LengthError:
                self.ui_utils.print_employee(employee, header)
                print('\033[31mInvalid Address\033[0m, please use format "streetname streetnumber"')

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
                self.ui_utils.print_employee(employee, header)
                print("\033[31mInvalid Value\033[0m, please enter a valid phone number")

            except LengthError:
                self.ui_utils.print_employee(employee, header)
                print("\033[31mInvalid Length\033[0m,Please input a valid phone number")
            
            
        self.data_wrapper.register_employee(employee)
        
        input(f"{employee.name} is successfully created! Press \033[34m[ENTER]\033[0m to exit: ")
