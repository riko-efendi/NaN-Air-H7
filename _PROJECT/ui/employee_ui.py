from model.employee import Employee
from utils.ui_utils import UIUtils
from ui.register_employee_ui import RegisterEmployeeUI
from ui.cabincrew_ui import CabinCrewUI

from ui.pilot_ui import PilotUI


class EmployeeUI:
    def __init__(self, wrapper) -> None:
       self.logic_wrapper = wrapper
       self.ui_utils = UIUtils()
       self.input_str = "Enter your choice: "

    def menu_output(self):
        self.ui_utils.clear_screen()
        print(f"[EMPLOYEES]\n")
        print(f"1. List all employees")
        print(f"2. Pilot")
        print(f"3. Cabin crew")
        print(f"\n[B]ack")

    def input_prompt(self):
        """ Takes in input from user """
        while True:
            self.menu_output()
            user_input = input("\n" + self.input_str).lower()

            if user_input == "b":
                break

            elif user_input == "1":
                self.ui_utils.clear_screen()
                employees = self.logic_wrapper.get_all_employees()
                print("[ALL EMPLOYEES]\n")

                for index, employee in enumerate(employees):
                    print(f"{index+1:>2}.{' name: ':^2}{employee.name:<}, {employee.role}\n      {'kt: ' + employee.print_kennitala}")

                input("\nPress [ENTER] to exit: ")

            elif user_input == "2":
                pilot_menu = PilotUI(self.logic_wrapper)
                back_method = pilot_menu.input_prompt()
                if back_method == "q":
                    return "q"
                pass
            elif user_input == "3":
                cabincrew_menu = CabinCrewUI(self.logic_wrapper)
                back_method = cabincrew_menu.input_prompt()
                if back_method == "q":
                    return "q"
                pass
            else:
                self.input_str = "Invalid. Enter another choice: "
