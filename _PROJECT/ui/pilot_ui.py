from logic.logic_wrapper import LogicWrapper
from ui.register_employee_ui import RegisterEmployeeUI
from model.employee import Employee

from utils.ui_utils import UIUtils
import time

DASH_AMOUNT = 46

class PilotUI:
    def __init__(self, logic_connection:LogicWrapper) -> None:
       self.logic_wrapper = logic_connection
       self.ui_utils = UIUtils()
       self.input_prompt_str = "Enter your choice: "

    def menu_output(self):
        """Prints out the options for the Pilot UI"""
        header = "[PILOTS]"
        self.ui_utils.clear_screen()
        print(header + "-" * (DASH_AMOUNT - len(header)) + "\n")
        print("\n" * 3)
        print(f"\t1. Register Pilot\n")
        print(f"\t2. View All Pilots\n")
        print(f"\t3. View Pilots by License\n")
        print("\n" * 3)
        print(f"\t\t\t\t\t[B]ack")
        print("-" * DASH_AMOUNT)




    def input_prompt(self):
        """Takes in an input from user, and jumpst to a specific UI/function based on that input."""

        user_input = ""

        while user_input != "b":
            self.menu_output()
            user_input = input("\n" + self.input_prompt_str).lower()

            if user_input == "1":
                register_employee_menu = RegisterEmployeeUI(self.logic_wrapper)
                e = Employee(role="Pilot")
                register_employee_menu.register_employee(e, "[REGISTER PILOT]")  
                self.input_prompt_str = "Enter your choice: "

            elif user_input == "2":
                self.list_all_pilots()
                self.input_prompt_str = "Enter your choice: "

            elif user_input == "3":
                self.view_pilots_by_license()
                self.input_prompt_str = "Enter your choice: "
            
            else:
                self.input_prompt_str = "\033[31mInvalid\033[0m. Enter another choice: "


    def list_all_pilots(self):
        """Lists all pilots from the crew.csv file"""
        header = "[ALL PILOTS]"
        self.ui_utils.clear_screen()
        pilots = self.logic_wrapper.get_all_pilots()
        print(header + "-" * (DASH_AMOUNT - len(header)) + "\n\n")
        for pilot in pilots:
            print(f"{pilot.name:^46}")
        print("\n\n" + "-" * DASH_AMOUNT)
        input("\nPress \033[34m[ENTER]\033[0m to exit: ")


    def view_pilots_by_license(self):
        """Gets the aircraft types, prints pilots by the inputed aircraft type"""
        
        aircrafts = self.logic_wrapper.get_all_aircraft_type()
        aircrafts_dict = {str(index + 1): value for index, value in enumerate(aircrafts)}
        license_type_input = self.print_pilot_list_by_license("Enter in a choice: ", aircrafts_dict)

        while license_type_input not in aircrafts_dict:
            license_type_input = self.print_pilot_list_by_license("\033[31mInvalid Input\033[0m. Enter another choice: ", aircrafts_dict)
        aircraft_type = aircrafts_dict[license_type_input]
        self.ui_utils.clear_screen()
        print("-" * DASH_AMOUNT)
        print(f"Showing pilot(s) for \033[32m{aircraft_type}\033[0m license")
        print("-" * DASH_AMOUNT + "\n")
        print("\n" * 3)
        for pilot in self.logic_wrapper.get_all_pilots_by_license(aircraft_type):
            print(f"{pilot:^46}")
        print("\n" * 3)
        print("\n" + "-" * DASH_AMOUNT)
        input("\nPress \033[34m[ENTER]\033[0m to exit: ")


    def print_pilot_list_by_license(self, input_str, a_dict):
        """Prints out different aircraft types based on an inputed dictinoary"""
        header = "[PILOT LIST BY AIRCRAFT LICENSE]"
        self.ui_utils.clear_screen()
        print(header + "-" * (DASH_AMOUNT - len(header)) + "\n")
        print("\n" * 3)
        for index, aircraft in a_dict.items():
            print(f"{index:>15}. {aircraft}\n")
        print("\n" * 3)
        print("\n" + "-" * DASH_AMOUNT)
        return input("\n" + input_str)
