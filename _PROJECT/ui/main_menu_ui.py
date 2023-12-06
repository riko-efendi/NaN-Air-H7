#from logic.logic_wrapper import LogicWrapper
from logic.logic_wrapper import LogicWrapper
from ui.employee_ui import EmployeeUI
from ui.voyage_ui import VoyageUI
#from funclibrary.functions import clear_screen

class MainMenuUI:
    def __init__(self) -> None:
       self.logic_wrapper = LogicWrapper()

    def menu_output(self):
        header = f"[MAIN]"
        
        print()
        print(header)
        print()
        print(f"1. Employees")
        print(f"2. Voyage")
        print(f"q. Quit")

    def input_prompt(self):
        while True:
            self.menu_output()
            user_input = input("\nEnter your choice: ").lower()
            #clear_screen()
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
