from logic.logic_wrapper import LogicWrapper
from ui.employee_ui import EmployeeUI
from ui.voyage_ui import VoyageUI
from utils.ui_utils import UIUtils


class MainMenuUI:
    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()
        self.ui_utils = UIUtils()
        self.input_prompt_str = "Enter your choice: "
        self.options = "1. Employees\n\n2. Voyage\n\n\n[Q]uit    [R]eset Terminal"

    def menu_output(self) -> None:
        """Prints out the options for the Main Menu UI"""
        self.ui_utils.clear_screen()
        print(self.ui_utils.append_string(self.ui_utils.make_boarder("MAIN"), self.options,-10 ,10))

    def input_prompt(self) -> None:
        """Takes in an input from user, and jumpst to a specific UI/function based on that input."""

        user_input = ""

        while user_input != "q":
            self.menu_output()
            user_input = input(self.input_prompt_str).lower()

            if user_input == "1":
                employee_menu = EmployeeUI(self.logic_wrapper)
                employee_menu.input_prompt()
                self.input_prompt_str = "Enter your choice: "
                
            elif user_input == "2":
                voyage_menu = VoyageUI(self.logic_wrapper)
                voyage_menu.input_prompt()
                self.input_prompt_str = "Enter your choice: "

            elif user_input == "r":
                self.menu_output()


            else:
                self. input_prompt_str = "Invalid. Enter another choice: "
            
            

        print("\nQUITTING")