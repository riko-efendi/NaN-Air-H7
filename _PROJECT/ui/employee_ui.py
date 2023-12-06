from model.employee import Employee
from utils.ui_utils import UIUtils
from ui.cabincrew_ui import CabinCrewUI
from ui.list_employee_ui import ListEmployeeUI
from ui.register_employee_ui import RegisterEmployeeUI
from ui.pilot_ui import PilotUI



class EmployeeUI:
    def __init__(self, wrapper) -> None:
       self.logic_wrapper = wrapper
       self.ui_utils = UIUtils()
       self.input_str = "Enter your choice: "

    def menu_output(self):

        self.ui_utils.clear_screen()
        print(f"[EMPLOYEES]\n")

        print(f"1. View Employees Options")
        print(f"2. Pilot")
        print(f"3. Cabin Crew")
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
                list_employees_menu = ListEmployeeUI(self.logic_wrapper)
                back_method = list_employees_menu.input_prompt()
                if back_method == "q":
                    return "q"


            elif user_input == "2":
                register_employee_menu = RegisterEmployeeUI(self.logic_wrapper)
                e = Employee()
                register_employee_menu.register_employee(e)


            elif user_input == "2":
                pilot_menu = PilotUI(self.logic_wrapper)
                back_method = pilot_menu.input_prompt()
                if back_method == "b":
                    break
                
            elif user_input == "3":
                cabincrew_menu = CabinCrewUI(self.logic_wrapper)
                back_method = cabincrew_menu.input_prompt()
                if back_method == "q":
                    return "q"
                
            else:
                self.input_str = "Invalid. Enter another choice: "
