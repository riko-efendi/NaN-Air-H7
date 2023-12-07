from logic.logic_wrapper import LogicWrapper
from ui.register_employee_ui import RegisterEmployeeUI
from model.employee import Employee

from utils.ui_utils import UIUtils

class PilotUI:
    def __init__(self, wrapper) -> None:
       self.logic_wrapper = wrapper
       self.ui_utils = UIUtils()
       self.input_prompt_str = "Enter your choice: "

    def menu_output(self):
        """Prints out the options for the Pilot UI"""

        self.ui_utils.clear_screen()
        print(f"[PILOTS]\n")
        print(f"1. Register pilot")
        print(f"2. List All pilots")
        print(f"3. View specific pilot")
        print(f"\n[B]ack")


    def input_prompt(self):
        """Takes in an input from user, and jumpst to a specific UI/function based on that input."""

        user_input = ""

        while user_input != "b":
            self.menu_output()
            user_input = input("\n" + self.input_prompt_str).lower()

            if user_input == "1":
                e = Employee()
                register_employee_menu = RegisterEmployeeUI(self.logic_wrapper)
                register_employee_menu.register_pilot(e)   

            elif user_input == "2":
                self.list_all_pilots()

            elif user_input == "3":
                self.view_specific_pilot()
            
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


    def view_specific_pilot(self):


        self.ui_utils.clear_screen()
        license_types = {
            "1": "NAFokkerF28",
            "2": "NAFokkerF100",
            "3": "NABAE146"}
        print("[PILOT LIST BY LICENCE]\n")

        while True:
            print("1. NAFokkerF28 2. NAFokkerF100 3. NABAE146")
            license_type_input = input("\nEnter License Type (1, 2, or 3): ")
            if license_type_input in license_types:
                license_type_input = license_types[license_type_input]
                break
            else:
                print("Invalid input. Please enter 1, 2, or 3.")

        print(f"\nShowing pilot(s) for {license_type_input}\n")
        print(self.logic_wrapper.get_all_pilots_by_license(license_type_input))
        input("\nPress [ENTER] to exit: ")