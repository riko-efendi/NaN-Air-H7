from utils.ui_utils import UIUtils
from ui.cabincrew_ui import CabinCrewUI
from ui.list_employee_ui import ListEmployeeUI
from ui.pilot_ui import PilotUI


class EmployeeUI:
    def __init__(self, wrapper) -> None:
       self.logic_wrapper = wrapper
       self.ui_utils = UIUtils()
       self.input_str = "Enter your choice: "

    def menu_output(self):

        self.ui_utils.clear_screen()
        print(f"[EMPLOYEES]\n")
        print(f"1. View Employees Options")
        print(f"2. Pilot")
        print(f"3. Cabin Crew")
        print(f"\n[B]ack")

    def input_prompt(self):
        """Takes in an input from user, and jumpst to a specific UI/function based on that input."""

        user_input = ""

        while user_input != "b":
            self.menu_output()
            user_input = input("\n" + self.input_str).lower()

            if user_input == "1":
                self.ui_utils.clear_screen()
                list_employees_menu = ListEmployeeUI(self.logic_wrapper)
                list_employees_menu.input_prompt()

            elif user_input == "2":
                pilot_menu = PilotUI(self.logic_wrapper)
                pilot_menu.input_prompt()
                
            elif user_input == "3":
                cabincrew_menu = CabinCrewUI(self.logic_wrapper)
                cabincrew_menu.input_prompt()

            else:
                self.input_str = "Invalid. Enter another choice: "
