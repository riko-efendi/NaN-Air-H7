from logic.logic_wapper import LogicWrapper
import os

class EmployeeUI:
    def __init__(self, wrapper) -> None:
       self.logic_wrapper = wrapper

    def menu_output(self):
        header = f"[EMPLOYEES]"
        os.system("cls")
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
            else:
                print("Invalid")