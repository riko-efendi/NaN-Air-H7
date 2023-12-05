from logic.logic_wrapper import LogicWrapper
from ui.register_employee_ui import RegisterEmployeeUI
from model.employee import Employee

class PilotUI:
    def __init__(self, wrapper) -> None:
       self.logic_wrapper = LogicWrapper()

    def menu_output(self):
        header = f"[PILOTS]"
        
        print()
        print(header)
        print()
        print(f"1. Register pilot")
        print(f"2. List All pilots")
        print(f"3. View specific pilot")
        print(f"q. Quit")

    def input_prompt(self):
        """ Takes in input from user """
        while True:
            self.menu_output()
            user_input = input("\nEnter your choice: ").lower()
            if user_input == "q":
                print("Quitting")
                break

            elif user_input == "1":
                register_employee_menu = RegisterEmployeeUI(self.logic_wrapper)
                e = Employee()
                register_employee_menu.register_pilot(e)   

            elif user_input == "2":
                pilots = self.logic_wrapper.get_all_pilots()
                print()
                print("[All Pilots]\n")
                for index, pilot in enumerate(pilots):
                    print(f"{index+1:>2}.{' name: ':^2}{pilot.name:<}, {'Role: '}{pilot.role}")

