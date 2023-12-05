from logic.employee_logic import EmployeeLogic
from model.employee import Employee
from utils.utils import UIUtils
from ui.pilot_ui import PilotUI
from ui.cabin_crew_ui import CabinCrewUI


class EmployeeUI:
    def __init__(self, wrapper) -> None:
       self.logic_wrapper = wrapper
       self.ui_utils = UIUtils()

    def menu_output(self):
        header = f"[EMPLOYEES]"
        
        print()
        print(header)
        print()
        print(f"1. List all employees")
        print(f"2. Pilot")
        print(f"3. Cabin crew")
        print(f"q. Quit")

    def input_prompt(self):
        """ Takes in input from user """
        while True:
            self.menu_output()
            user_input = input("\nEnter your choice: ").lower()
            # Clears screen
            # self.ui_utils.clear_screen()
            if user_input == "q":
                print("Quitting")
                break
            elif user_input == "1":
                employees = self.logic_wrapper.get_all_employees()
                print()
                print("[ALL EMPLOYEES]")
                print()
                for index, employee in enumerate(employees):
                    print(f"{index+1:>2}.{' name: ':^2}{employee.name:<}, {employee.role}\n      {'kt: ' + employee.print_kennitala}")
            elif user_input == "2":
                pilot_menu = PilotUI(self.logic_wrapper)
                back_method = pilot_menu.input_prompt()
                if back_method == "q":
                    return "q"
                pass
            elif user_input == "3":
                cabin_crew_menu = CabinCrewUI(self.logic_wrapper)
                back_method = cabin_crew_menu.input_prompt()
                if back_method == "q":
                    return "q"
                pass
            else:
                print("Invalid")