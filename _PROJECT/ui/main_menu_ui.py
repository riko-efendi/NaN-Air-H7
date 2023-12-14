from logic.logic_wrapper import LogicWrapper
from ui.employee_ui import EmployeeUI
from ui.voyage_ui import VoyageUI
from utils.ui_utils import UIUtils

DASH_AMOUNT = 46

class MainMenuUI:
    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()
        self.ui_utils = UIUtils()
        self.input_prompt_str = "Enter your choice: "

    def menu_output(self) -> None:
        """Prints out the options for the Main Menu UI"""

        header = "[Main Menu]"
        self.ui_utils.clear_screen()
        print(header + "-" * (DASH_AMOUNT - len(header)) + "\n")
        print("\n" * 4)
        print(f"\t1. Employees\n")
        print(f"\t2. Voyage\n")
        print("\n" * 4)
        print(f"\t\t\t\t\t[Q]uit")
        print("-" * DASH_AMOUNT)

    def input_prompt(self) -> None:
        """Takes in an input from user, and jumpst to a specific UI/function based on that input."""

        user_input = ""

        while user_input != "q":
                self.menu_output()
                user_input = input("\n" + self.input_prompt_str).lower()

                if user_input == "1":
                    employee_menu = EmployeeUI(self.logic_wrapper)
                    employee_menu.input_prompt()
                    self.input_prompt_str = "Enter your choice: "
                    
                elif user_input == "2":
                    voyage_menu = VoyageUI(self.logic_wrapper)
                    voyage_menu.input_prompt()
                    self.input_prompt_str = "Enter your choice: "
                else:
                    self. input_prompt_str = "\033[31mInvalid input.\033[0m Enter another choice: "

        print("\nQUITTING")