from logic.logic_wrapper import LogicWrapper
from ui.register_employee_ui import RegisterEmployeeUI
from model.employee import Employee

from utils.ui_utils import UIUtils

class PilotUI:
    def __init__(self, wrapper) -> None:
       self.logic_wrapper = wrapper
       self.ui_utils = UIUtils()
       self.input_str = "Enter your choice: "

    def menu_output(self):
        self.ui_utils.clear_screen()
        print(f"[PILOTS]\n")
        print(f"1. Register pilot")
        print(f"2. List All pilots")
        print(f"3. View specific pilot")
        print(f"\n[B]ack")

    def input_prompt(self):
        """ Takes in input from user """
        while True:
            self.menu_output()
            user_input = input("\n" + self.input_str).lower()
            if user_input == "B":
                break

            elif user_input == "1":
                register_employee_menu = RegisterEmployeeUI(self.logic_wrapper)
                e = Employee()
                register_employee_menu.register_pilot(e)   

            elif user_input == "2":
                self.ui_utils.clear_screen()
                pilots = self.logic_wrapper.get_all_pilots()
                print("[ALL PILOTS]\n")
                for index, pilot in enumerate(pilots):
                    print(f"{index+1:>2}.{' name: ':^2}{pilot.name:<}, {'Role: '}{pilot.role}")
                input("\nPress [ENTER] to exit: ")

            elif user_input == "3":
                self.ui_utils.clear_screen()
                plane_type_input = input("Enter Plane Type: ")
                print(f"\nShowing pilot(s) for {plane_type_input}\n")
                print(self.logic_wrapper.get_all_pilots_by_license(plane_type_input))
                input("\nPress [ENTER] to exit: ")
            
            else:
                self.input_str = "Invaild. Enter another choice: "