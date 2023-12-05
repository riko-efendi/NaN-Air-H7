from logic.employee_logic import EmployeeLogic
from model.employee import Employee
from utils.utils import UIUtils
from ui.pilot_ui import PilotUI


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
        print(f"2. Register employee (temporary)")
        print(f"3. Pilot")
        print(f"4. Cabin crew")
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
                print("\n[REGISTER EMPLOYEE]\N")
                e = Employee()
                e.name = input("Input the employee name: ")
                e.kennitala = input("Input the employee kennitala: ")
                e_rank = input("Is the employee a [P]ilot or [C]abincrew? P/C: ").lower()
                while e_rank != "p" or e_rank != "c":
                    e_rank = input("Is the employee a [P]ilot or [C]abincrew? P/C: ").lower()
                if e_rank == "p":
                    e.role = "Pilot"
                elif e_rank == "c":
                    e.role = "Cabincrew"
                
                self.logic_wrapper.register(e)

            elif user_input == "3":
                pilot_menu = PilotUI(self.logic_wrapper)
                back_method = pilot_menu.input_prompt()
                if back_method == "q":
                    return "q"
                pass
            else:
                print("Invalid")