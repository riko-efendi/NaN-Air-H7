from logic.logic_wrapper import LogicWrapper
from model.employee import Employee
from ui.register_employee_ui import RegisterEmployeeUI

from utils.ui_utils import UIUtils

class CabinCrewUI:
    def __init__(self, wrapper) -> None:
       self.logic_wrapper = wrapper
       self.ui_utils = UIUtils()

    def menu_output(self):        
        self.ui_utils.clear_screen()

        print(f"[CABIN CREW]\n")
        print(f"1. Register cabin crew")
        print(f"2. List All cabin crews")
        print(f"3. View specific cabin crew")
        print(f"\n[B]ack")

    def input_prompt(self):
        """ Takes in input from user """
        while True:
            self.menu_output()
            user_input = input("\nEnter your choice: ").lower()

            if user_input == "b":
                break

            elif user_input == "1":
                register_employee_menu = RegisterEmployeeUI(self.logic_wrapper)
                e = Employee()
                register_employee_menu.register_cabin_crew(e)   

            elif user_input == "2":
                cabincrews = self.logic_wrapper.get_all_cabincrews()
                self.ui_utils.clear_screen()
                print("[ALL CABIN CREW]\n")
                for index, cabincrew in enumerate(cabincrews):
                    print(f"{index+1:>2}.{' Name: ':^2}{cabincrew.name:<}, {'Role: '}{cabincrew.role}")
                input("\nPress [ENTER] to exit: ")
                