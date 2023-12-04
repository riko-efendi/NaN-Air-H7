from logic.logic_wapper import LogicWrapper
from ui.employee_ui import EmployeeUI
from ui.voyage_ui import VoyageUI
import os

class MainMenuUI:
    def __init__(self) -> None:
       self.logic_wrapper = LogicWrapper()

    def menu_output(self):
        header = f"[MAIN]"
        os.system("cls")
        print(header)
        print()
        print(f"1. Employees")
        print(f"2. Voyage")
        print(f"q. Quit")

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
                if back_method == "b":
                    return "q"
                pass
            elif user_input == "2":
                employee_menu = VoyageUI(self.logic_wrapper)
                back_method = employee_menu.input_prompt()
                if back_method == "b":
                    return "q"
                pass
            else:
                print("Invalid")
