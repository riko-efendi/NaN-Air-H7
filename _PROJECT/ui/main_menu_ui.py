from logic.logic_wrapper import LogicWrapper
from ui.employee_ui import EmployeeUI
from ui.voyage_ui import VoyageUI

from utils.ui_utils import UIUtils


class MainMenuUI:
    def __init__(self) -> None:
       self.logic_wrapper = LogicWrapper()
       self.ui_utils = UIUtils()

    def menu_output(self):

        options = "1. Employees\n2. Voyage\n\nEnter a number or [Q]uit"
        boarder = self.ui_utils.get_boarder("[MAIN MENU]", options, 0, 5)
        self.ui_utils.clear_screen()
        print(boarder)

    def input_prompt(self):

        while True:
            self.menu_output()
            user_input = input("Enter your choice: ").lower()
            if user_input == "q":
                print("Quitting")
                break
            elif user_input == "1":
                employee_menu = EmployeeUI(self.logic_wrapper)
                back_method = employee_menu.input_prompt()
                if back_method == "q":
                    return "q"
                pass
            elif user_input == "2":
                voyage_menu = VoyageUI(self.logic_wrapper)
                back_method = voyage_menu.input_prompt()
                if back_method == "q":
                    return "q"
                pass
            else:
                print("Invalid")
