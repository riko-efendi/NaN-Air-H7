from logic.logic_wrapper import LogicWrapper
from ui.employee_ui import EmployeeUI
from ui.voyage_ui import VoyageUI
from ui.NaN_Air_Ascii import ART # þetta er Logo-ið
from utils.ui_utils import UIUtils

class MainMenuUI:
    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()
        self.ui_utils = UIUtils()
        self.input_str = "Enter your choice: "
        self.ascii = ART

    def menu_output(self):
        self.ui_utils.clear_screen()
        print(f"{ART}") # Hér er logo-ið að printast, getum alltaf breytt logo-inu. 
        print(f"[MAIN]\n")
        print(f"1. Employees")
        print(f"2. Voyage")
        print(f"\n[Q]uit")

    def input_prompt(self):
        while True:
            self.menu_output()
            user_input = input("\n" + self.input_str).lower()
            if user_input == "q":
                print("\nQUITTING\n")
                break

            elif user_input == "1":
                employee_menu = EmployeeUI(self.logic_wrapper)
                back_method = employee_menu.input_prompt()
                if back_method == "q":
                    return "q"
                
            elif user_input == "2":
                voyage_menu = VoyageUI(self.logic_wrapper)
                back_method = voyage_menu.input_prompt()
                if back_method == "q":
                    return "q"
               
            else:
                self. input_str = "Invalid. Enter another choice: "
