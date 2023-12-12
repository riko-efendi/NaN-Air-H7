from utils.ui_utils import UIUtils
from prettytable import PrettyTable
class ListEmployeeUI:
    def __init__(self, wrapper) -> None:
        self.logic_wrapper = wrapper
        self.ui_utils = UIUtils()
        self.input_prompt_str = "Enter your choice: "

    def menu_output(self) -> None:
        """Prints out the options for the Employee Options Menu UI"""

        self.ui_utils.clear_screen()
        print(f"[VIEW EMPLOYEE OPTIONS]\n")
        print(f"1. View all employees")
        print(f"2. View Employee By Kennitala")
        print(f"3. View Off Duty Employees")
        print(f"4. View On Duty Employees")
        print(f"\n[B]ack")

    def input_prompt(self) -> None:
        """"Takes in an input from user, and jumpst to a specific UI/function based on that input."""

        user_input = ""

        while user_input != "b":
            self.menu_output()
            user_input = input("\n" + self.input_prompt_str).lower()
            if user_input == "1":
                self.view_all_employees()
            elif user_input == "2":
                self.view_employee_by_kennitala()
            else:
                self.input_prompt_str = "Invalid. Enter another choice: "

    def view_all_employees(self) -> None:
        """Prints out every employee registered in the crew.csv file."""

        employees = self.logic_wrapper.get_all_employees()
        self.ui_utils.clear_screen()
        print("[ALL EMPLOYEES]\n")
        
    

        # Create a PrettyTable instance and define columns
        table = PrettyTable()
        table.field_names = ["Index", "Name", "Role", "Rank", "Kennitala", "Heimilisfang"]

        # Populate the table with data
        for index, employee in enumerate(employees):
            table.add_row([index+1, employee.name, employee.role, employee.rank, employee.print_kennitala, employee.address])

        # Print the formatted table
        print(table)

        input("\nPress [ENTER] to exit: ")
        """for index, employee in enumerate(employees):
            print(f"{index+1:>2}.{' name: ':^2}{employee.name:<}, {employee.role}\n      {'kt: ' + employee.print_kennitala}")
        input("\nPress [ENTER] to exit: ")"""


    def print_update_employee_info(self, name, kennitala, address, role, rank, phone_number):
        self.ui_utils.clear_screen()
        print("[UPDATE EMPLOYEE INFO]\n")
        self.print_employee(name, kennitala, address, role, rank, phone_number)


    def print_employee(self, name, kennitala, address, role, rank, phone_number) -> None:
        print(f"Name: {name}")
        print(f"Kt: {kennitala}")
        print(f"Address: {address}")
        print(f"Role: {role}")
        print(f"Rank: {rank}")
        print(f"Phone number: {phone_number}")


    def view_employee_by_kennitala(self):
        self.ui_utils.clear_screen()
        kennitala_input = input("Enter Employee Kennitala: ")
        employee = self.logic_wrapper.get_employee_by_nid(kennitala_input)
        self.ui_utils.clear_screen()
        print(f"[EMPLOYEE INFO]\n")
        self.print_employee(employee.name, employee.kennitala, employee.address, employee.role, employee.rank, employee.phone_number)

        print("\n[U]pdate Info\t[W]ork Schedule\t  [B]ack")
        option_input = input("\nEnter your choice: ").lower()

        if option_input == "u":
            self.print_update_employee_info(employee.name, employee.kennitala, employee.address, employee.role, employee.rank, employee.phone_number)
            new_address = input("\nEnter a new address or [K]eep old address: ")

            if new_address.lower() == "k":
                new_address = employee.address
            self.print_update_employee_info(employee.name, employee.kennitala, new_address.upper(), employee.role, employee.rank, employee.phone_number)
            new_phone_number = input("\nEnter a new phone number or [K]eep old phone number: ").lower()

            if new_phone_number.lower() == "k":
                new_phone_number = employee.phone_number
            self.print_update_employee_info(employee.name, employee.kennitala, new_address.upper(), employee.role, employee.rank, new_phone_number.upper())
            self.logic_wrapper.update_employee_info(kennitala_input, new_address, new_phone_number)
            print("\nSuccess!")
            input("\nPress [ENTER] to confirm: ")
            
        elif option_input == "w":
            self.ui_utils.clear_screen()
            print(f"[WORK SCHEDULE]\n")
            print("Insert beautiful work schedule here")
            input("Press [ENTER] to exit")
        
        elif option_input == "b":
            return None