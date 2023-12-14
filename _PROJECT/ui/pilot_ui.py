from logic.logic_wrapper import LogicWrapper
from ui.register_employee_ui import RegisterEmployeeUI
from model.employee import Employee
from utils.ui_utils import UIUtils
from utils.ascii_art import AsciiArt

DASH_AMOUNT = 38
SPACING = " " * 14

class PilotUI:
    def __init__(self, logic_connection:LogicWrapper) -> None:
       self.logic_wrapper = logic_connection
       self.ui_utils = UIUtils()
       self.input_prompt_str = "Enter your choice: "
       self.ascii_art = AsciiArt()

    def menu_output(self):
        """Prints out the options for the Pilot UI"""
        header = "[PILOTS]"
        self.ui_utils.clear_screen()
        print(self.ascii_art.nanair_logo(SPACING))
        print(header + "-" * (DASH_AMOUNT - len(header)) +"\n")
        print(f"{SPACING}1. Register pilot\n")
        print(f"{SPACING}2. List All pilots\n")
        print(f"{SPACING}3. View specific pilot")
        print(f"\t\t\t\t[B]ack")
        print("-"*DASH_AMOUNT)


    def input_prompt(self):
        """Takes in an input from user, and jumpst to a specific UI/function based on that input."""

        user_input = ""

        while user_input != "b":
            self.menu_output()
            user_input = input(self.input_prompt_str).lower()

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
                self.input_prompt_str = "Invaild. Enter another choice: "


    def list_all_pilots(self):
        """Lists all pilots from the crew.csv file"""

        self.ui_utils.clear_screen()
        pilots = self.logic_wrapper.get_all_pilots()
        print("[ALL PILOTS]\n")
        for index, pilot in enumerate(pilots):
            print(f"{index + 1:>2}.{' Name: ':^2}{pilot.name:<}, {'Rank: '}{pilot.rank}")
        input("\nPress [ENTER] to exit: ")


    def view_pilots_by_license(self):
        """Gets the aircraft types, prints pilots by the inputed aircraft type"""
        
        aircrafts = self.logic_wrapper.get_all_aircraft_type()
        aircrafts_dict = {str(index + 1): value for index, value in enumerate(aircrafts)}
        license_type_input = self.print_pilot_list_by_license("Enter in a choice: ", aircrafts_dict)

        while license_type_input not in aircrafts_dict:
            license_type_input = self.print_pilot_list_by_license("Invalid. Enter another choice: ", aircrafts_dict)
            
        aircraft_type = aircrafts_dict[license_type_input]
        print(f"\nShowing pilot(s) for {aircraft_type}\n")
        print(self.logic_wrapper.get_all_pilots_by_license(aircraft_type))
        input("\nPress [ENTER] to exit: ")


    def print_pilot_list_by_license(self, input_str, a_dict):
        """Prints out different aircraft types based on an inputed dictinoary"""

        self.ui_utils.clear_screen()
        print("[PILOT LIST BY AIRCRAFT LICENCE]\n")
        for index, aircraft in a_dict.items():
            print(f"{index}. {aircraft}")
        return input("\n" + input_str)
