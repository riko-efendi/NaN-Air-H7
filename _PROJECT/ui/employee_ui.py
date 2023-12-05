from logic.employee_logic import EmployeeLogic
from model.employee import Employee
from ui.pilot_ui import PilotUI
from ui.register_employee_ui import RegisterEmployeeUI
from ui.cabincrew_ui import CabinCrewUI
from utils.ui_utils import UIUtils



class EmployeeUI:
    def __init__(self, wrapper) -> None:
       self.logic_wrapper = wrapper
       self.ui_utils = UIUtils()

    def menu_output(self):

        options = "1. List All Employees\n2. Pilot\n3. Cabin Crew\n\n[B]ack"
        boarder = self.ui_utils.get_boarder("[EMPLOYEE MENU]", options, 0, 5)
        self.ui_utils.clear_screen()
        print(boarder)

    def input_prompt(self):
        """ Takes in input from user """
        while True:
            self.menu_output()
            user_input = input("Enter your choice: ").lower()
            if user_input == "b":
                print("Quitting")
                break

            elif user_input == "1":

                self.ui_utils.clear_screen()

                employees = self.logic_wrapper.get_all_employees()
                print("[ALL EMPLOYEES]")
                print()
                for index, employee in enumerate(employees):
                    print(f"{index+1:>2}.{' name: ':^2}{employee.name:<}, {employee.role}\n      {'kt: ' + employee.print_kennitala}")
                input("\nPress any key to exit: ")

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
                print("Invalid")
