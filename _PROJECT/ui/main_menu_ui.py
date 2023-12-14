from logic.logic_wrapper import LogicWrapper
from ui.employee_ui import EmployeeUI
from ui.voyage_ui import VoyageUI
from utils.ui_utils import UIUtils
from utils.ascii_art import AsciiArt

DASH_AMOUNT = 38
SPACING = " " * int((DASH_AMOUNT -10)/2)
LOGO_SPACING = " " * int((DASH_AMOUNT -10)/4)

class MainMenuUI:
    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()
        self.ui_utils = UIUtils()
        self.input_prompt_str = "Enter your choice: "
        self.asdcii_art = AsciiArt()

    def menu_output(self) -> None:
        """Prints out the options for the Main Menu UI"""
        header = "[MAIN]"
        self.ui_utils.clear_screen()
        print(self.asdcii_art.nanair_logo(LOGO_SPACING))
        print(header + "-" * (DASH_AMOUNT - len(header)) +"\n")
        print(f"{SPACING}1. Employees\n")
        print(f"{SPACING}2. Voyage")
        print("\n"*8)
        print(f"{' ' * (DASH_AMOUNT - len('[Q]uit'))}[Q]uit")
        print("-"*DASH_AMOUNT)


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

            else:
                self. input_prompt_str = "Invalid. Enter another choice: "
            