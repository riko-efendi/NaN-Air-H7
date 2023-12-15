from datetime import datetime
from utils.ui_utils import UIUtils
from logic.logic_wrapper import LogicWrapper
from ui.input_validation import LengthError, validate_length_kt, validate_integers, validate_date_format

import time

DASH_AMOUNT = 46

class ListEmployeeUI:
    def __init__(self, logic_connection:LogicWrapper) -> None:
        self.logic_wrapper = logic_connection
        self.ui_utils = UIUtils()
        self.input_prompt_str = "Enter your choice: "

    def menu_output(self) -> None:
        """Prints out the options for the Employee Options Menu UI"""
        header = "[VIEW EMPLOYEE OPTIONS]"
        self.ui_utils.clear_screen()
        print(header + "-" * (DASH_AMOUNT - len(header)) + "\n")
        print("\n" * 2)
        print(f"\t1. View All employees\n")
        print(f"\t2. View Employee By Kennitala\n")
        print(f"\t3. View Off Duty Employees\n")
        print(f"\t4. View On Duty Employees\n")
        print("\n" * 2)
        print(f"\t\t\t\t\t[B]ack")
        print("-" * DASH_AMOUNT)

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

            elif user_input == "3":
                self.view_off_duty_employees()

            elif user_input == "4":
                self.view_on_duty_employees_by_date()

            else:
                self.input_prompt_str = "\033[31mInvalid.\033[0m Enter another choice: "

    def view_all_employees(self) -> None:
        """Prints out every employee registered in the crew.csv file."""
        header = "[ALL EMPLOYEES]"
        employees = self.logic_wrapper.get_all_employees()
        self.ui_utils.clear_screen()
        print(header + "-" * (DASH_AMOUNT - len(header)) + "\n")
        for index, employee in enumerate(employees):
            print(f"{index+1}. {employee.name} - {employee.role}\n    {'kt: ' + employee.print_kennitala}\n")

        print("-" * DASH_AMOUNT)
        input("\nPress \033[34m[ENTER]\033[0m to exit: ")

    def print_update_employee_info(self, name, kennitala, address, role, rank, phone_number):
        header = "[UPDATE EMPLOYEE INFO]"
        self.ui_utils.clear_screen()
        print(header + "-" * (DASH_AMOUNT - len(header)) + "\n")
        print("\n" * 3)
        self.print_employee(name, kennitala, address, role, rank, phone_number)
        print("\n" * 3)
        print("\n" + "-" * DASH_AMOUNT)
        
    def print_employee(self, name, kennitala, address, role, rank, phone_number) -> None:
        print(f"Name: {name:>18}")
        print(f"Kt: {kennitala:>15}")
        print(f"Address: {address}")
        print(f"Role: {role}")
        print(f"Rank: {rank}")
        print(f"Phone number: {phone_number}")


    def view_employee_by_kennitala(self):

        self.ui_utils.clear_screen()
        
        while True:
            try:
                header = "[View Employee by Kennitala]"
                print(header + "-" * (DASH_AMOUNT - len(header)) + "\n")
                print("\n" * 13)
                print(f"\t\t\t\t\t[B]ack")
                print("-" * DASH_AMOUNT + "\n")
                kennitala_input = input("Enter Employee Kennitala: ")
                
                validate_integers(kennitala_input)
                validate_length_kt(kennitala_input)
                employee = self.logic_wrapper.get_employee_by_nid(kennitala_input)
                if employee != None:
                    break
                else:
                    print(f"\033[31mNo Record of {kennitala_input}\033[0m")
                    time.sleep(1.5)
                    self.ui_utils.clear_screen()
            except ValueError:
                print("\033[31mInvalid value, please enter a valid kennitala\033[0m")
                time.sleep(1.5)
                self.ui_utils.clear_screen()
            except LengthError:
                print("\033[31mInvalid length, please enter a valid kennitala\033[0m")
                time.sleep(1.5)
                self.ui_utils.clear_screen()

        header = "[EMPLOYEE INFO]"        
        self.ui_utils.clear_screen()
        print(header + "-" * (DASH_AMOUNT - len(header)) + "\n")
        print("\n" * 2)
        self.print_employee(employee.name, employee.kennitala, employee.address, employee.role, employee.rank, employee.phone_number)

        print("\n" * 3)
        print("\n[U]pdate Info\t   [W]ork Schedule\t[B]ack")
        print("-" * DASH_AMOUNT)
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
            print("\n\033[32mSuccessfully Updated!\033[0m")
            input("\nPress \033[34m[ENTER]\033[0m to confirm: ")
            
        elif option_input == "w":
            self.view_work_schedule_by_date_range(employee.kennitala)
        
        elif option_input == "b":
            return None
    
    def view_work_schedule_by_date_range(self, kennitala):
        """Takes start_date and end_date inputs, then check kennitala using logic wrapper to print out employee's name"""
        header = "[WORK SUMMARY]"
        self.ui_utils.clear_screen()
        print(header + "-" * (DASH_AMOUNT - len(header)) + "\n")
        print("\n" * 13)
        print(f"\t\t\t\t\t[B]ack")
        print("-" * DASH_AMOUNT + "\n")
        start_date = input("Enter Start Date [YYYY-MM-DD]: ")
        end_date = input("Enter End Date [YYYY-MM-DD]: ")

        flights = self.logic_wrapper.get_employees_past_schedule_by_date_range_and_kennitala(start_date, end_date, kennitala)
        employee = self.logic_wrapper.get_employee_by_nid(kennitala)
        
        self.ui_utils.clear_screen()
        print("-" * DASH_AMOUNT)
        print(f"{employee.name}'s Work Schedule on {start_date} - {end_date}")
        print("-" * DASH_AMOUNT)
        print("\n" * 3)
        if flights:
            for flight in flights:
                print(f"Flight #: {flight['flight_nr']}, {flight['dep_from']} -> {flight['arr_at']}, Departure: {flight['departure_date']} {flight['departure_time']}, Arrival: {flight['arrival_date']} {flight['arrival_time']}")
        else:
            print("No flights scheduled for this employee within the specified date range.")
        print("\n" * 3)
        print("-" * DASH_AMOUNT)
        input("\nPress \033[34m[ENTER]\033[0m to exit: ")

    def view_on_duty_employees_by_date(self):
        header = "[View On Duty Employees By Date]"
        self.ui_utils.clear_screen()
        print(header + "-" * (DASH_AMOUNT - len(header)) + "\n")
        print("\n" * 13)
        print(f"\t\t\t\t\t[B]ack")
        print("-" * DASH_AMOUNT + "\n")
        date_input = input("Enter Date [YYYY-MM-DD]: ")
        flights = self.logic_wrapper.get_avaiable_fligths_by_date(date_input)
        self.ui_utils.clear_screen()

        print("-" * DASH_AMOUNT)
        print(f"ALL ON DUTY EMPLOYEES on \033[32m{date_input}\033[0m")
        print("-" * DASH_AMOUNT)
        print("\n" * 3)
        employees_printed = set() 

        for flight in flights:
            for employee_nid in flight.crew.values():
                if employee_nid not in employees_printed:
                    employee = self.logic_wrapper.get_employee_by_nid(employee_nid)
                    if employee: 
                        print(f"{employee.name:^22} \tDestination: {flight.arr_at}")
                    employees_printed.add(employee_nid)
        print("\n" * 3) 
        print("\n" + "-" * DASH_AMOUNT)
        input("\nPress \033[34m[ENTER]\033[0m to exit: ")

    def view_off_duty_employees(self):
        header = "[View Off Duty Employee by Date]"
        self.ui_utils.clear_screen()
        print(header + "-" * (DASH_AMOUNT - len(header)) + "\n")
        print("\n" * 13)
        print(f"\t\t\t\t\t[B]ack")
        print("-" * DASH_AMOUNT + "\n")
        date_input = input("Enter Date [YYYY-MM-DD]: ")

        while True:
            try:
                if date_input == "b":
                    break
                validate_date_format(date_input)
                on_duty_employees = set()
                flights = self.logic_wrapper.get_non_available_flights_by_date(date_input)                
                self.ui_utils.clear_screen()
                print("-" * DASH_AMOUNT)
                print(f"Off Duty Employees on \033[32m{date_input}\033[0m:")
                print("-" * DASH_AMOUNT + "\n")
                for flight in flights:
                    for employee_nid in flight.crew.values():
                        employee = self.logic_wrapper.get_employee_by_nid(employee_nid)
                        if employee and employee.kennitala not in on_duty_employees:
                            print(f"{employee.name:^22} {employee.rank:^22}")
                            on_duty_employees.add(employee.kennitala)
                print("\n" + "-" * DASH_AMOUNT)
                input("\nPress \033[34m[ENTER]\033[0m to exit: ")    
                break
            except ValueError:
                print("\033[31mInvalid input.\033[0m Enter a valid format date")
                time.sleep(1.5)
                self.ui_utils.clear_screen()