from logic.logic_wrapper import LogicWrapper
from ui.employee_ui import EmployeeUI
from ui.voyage_ui import VoyageUI
from utils.ui_utils import UIUtils


class MainMenuUI:
    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()
        self.ui_utils = UIUtils()
        self.input_str = "Enter your choice: "

    def menu_output(self) -> None:
        """Prints out the options for the Main Menu UI"""

        self.ui_utils.clear_screen()
        print(f"[MAIN]\n")
        print(f"1. Employees")
        print(f"2. Voyage")
        print(f"\n[Q]uit")

    def input_prompt(self) -> None:
        """Takes in an input from user, and jumpst to a specific UI/function based on that input."""

        user_input = ""

        while user_input != "b":
            self.menu_output()
            user_input = input("\n" + self.input_str).lower()

            if user_input == "1":
                employee_menu = EmployeeUI(self.logic_wrapper)
                employee_menu.input_prompt()
                
            elif user_input == "2":
                voyage_menu = VoyageUI(self.logic_wrapper)
                voyage_menu.input_prompt()
               
            else:
                self. input_str = "Invalid. Enter another choice: "

        print("\nQUITTING")