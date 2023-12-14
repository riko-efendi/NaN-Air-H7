from utils.ui_utils import UIUtils
from ui.cabincrew_ui import CabinCrewUI
from ui.list_employee_ui import ListEmployeeUI
from ui.pilot_ui import PilotUI
from utils.ascii_art import AsciiArt
from logic.logic_wrapper import LogicWrapper

DASH_AMOUNT = 38
SPACING = " " * 14

class EmployeeUI:
    def __init__(self, logic_connection:LogicWrapper) -> None:
       self.logic_wrapper = logic_connection
       self.ui_utils = UIUtils()
       self.input_prompt_str = "Enter your choice: "
       self.ascii_art = AsciiArt()

    def menu_output(self) -> None:
        """Prints out the options for the Employee UI"""
        
        header = "[EMPLOYEES]"
        self.ui_utils.clear_screen()
        print(self.ascii_art.nanair_logo(SPACING))
        print(header + "-" * (DASH_AMOUNT - len(header)) +"\n")
        print(f"{SPACING}1. View Employees Options\n")
        print(f"{SPACING}2. Pilot\n")
        print(f"{SPACING}3. Cabin Crew")
        print(f"\t\t\t\t[B]ack")
        print("-"*DASH_AMOUNT)

    def input_prompt(self) -> None:
        """Takes in an input from user, and jumpst to a specific UI/function based on that input."""

        user_input = ""

        while user_input != "b":
            self.menu_output()
            user_input = input(self.input_prompt_str).lower()

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
                self.input_prompt_str = "Invalid. Enter another choice: "
