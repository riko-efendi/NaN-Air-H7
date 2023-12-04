from logic.employee_logic import EmployeeLogic
from model.employee import Employee
from funclibrary.functions import clear_screen

class EmployeeUI:
    def __init__(self, wrapper) -> None:
       self.logic_wrapper = wrapper

    def menu_output(self):
        header = f"[EMPLOYEES]"
        # clear_screen()
        print(header)
        print()
        print(f"1. List all employees")
        print(f"2. Register employee")
        print(f"3. Pilot")
        print(f"4. Cabin crew")
        print(f"q. Quit")

    def input_prompt(self):
        while True:
            self.menu_output()
            user_input = input("Enter your choice: ").lower()
            if user_input == "q":
                print("Quitting")
                break
            elif user_input == "1":
                employees = self.logic_wrapper.get_all_employees()
                for employee in employees:
                    print(f"It fucking works {employee}")
            else:
                print("Invalid")