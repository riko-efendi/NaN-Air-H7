from utils.ui_utils import UIUtils
from ui.cabincrew_ui import CabinCrewUI
from ui.list_employee_ui import ListEmployeeUI
from ui.pilot_ui import PilotUI

DASH_AMOUNT = 46

class EmployeeUI:
    def __init__(self, wrapper) -> None:
       self.logic_wrapper = wrapper
       self.ui_utils = UIUtils()
       self.input_prompt_str = "Enter your choice: "

    def menu_output(self) -> None:
        """Prints out the options for the Employee UI"""
        header = "[EMPLOYEES]"
        self.ui_utils.clear_screen()
        print(header + "-" * (DASH_AMOUNT - len(header)) + "\n")
        print("\n" * 3)
        print(f"\t1. View Employees Options\n")
        print(f"\t2. Pilot\n")
        print(f"\t3. Cabin Crew\n")
        print("\n" * 3)
        print(f"\t\t\t\t\t[B]ack")
        print("-" * DASH_AMOUNT)

    def input_prompt(self) -> None:
        """Takes in an input from user, and jumpst to a specific UI/function based on that input."""

        user_input = ""

        while user_input != "b":
            self.menu_output()
            user_input = input("\n" + self.input_prompt_str).lower()

            if user_input == "1":
                self.ui_utils.clear_screen()
                list_employees_menu = ListEmployeeUI(self.logic_wrapper)
                list_employees_menu.input_prompt()
                self.input_prompt_str = "Enter your choice: "

            elif user_input == "2":
                pilot_menu = PilotUI(self.logic_wrapper)
                pilot_menu.input_prompt()
                self.input_prompt_str = "Enter your choice: "
                
            elif user_input == "3":
                cabincrew_menu = CabinCrewUI(self.logic_wrapper)
                cabincrew_menu.input_prompt()
                self.input_prompt_str = "Enter your choice: "

            else:
                self.input_prompt_str = "\033[31mInvalid input.\033[0m Enter another choice: "
