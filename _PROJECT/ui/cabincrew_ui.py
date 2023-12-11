from logic.logic_wrapper import LogicWrapper
from model.employee import Employee
from ui.register_employee_ui import RegisterEmployeeUI

from utils.ui_utils import UIUtils

class CabinCrewUI:
    def __init__(self, wrapper) -> None:
       self.logic_wrapper = wrapper
       self.ui_utils = UIUtils()
       

    def menu_output(self) -> None:
        """Prints out the options for the Cabin Crew UI"""
        
        self.ui_utils.clear_screen()
        print(f"[CABIN CREW]\n")
        print(f"1. Register cabin crew")
        print(f"2. List All cabin crews")
        print(f"3. View specific cabin crew")
        print(f"\n[B]ack")


    def input_prompt(self) -> None:
        """Takes in an input from user, and jumpst to a specific UI/function based on that input."""

        user_input = ""

        while user_input != "b":
            self.menu_output()
            user_input = input("\nEnter your choice: ").lower()

            if user_input == "1":
                self.regist_cabin_crew()

            elif user_input == "2":
                self.list_all_cabin_crew()


    def regist_cabin_crew(self) -> None:
        """Creates an employee and passes it to the Register Employee UI, where it is registered in the crew.csv file"""

        e = Employee()
        register_employee_menu = RegisterEmployeeUI(self.logic_wrapper)
        register_employee_menu.register_cabin_crew(e)   


    def list_all_cabin_crew(self) -> None:
        """Prints out all cabin crew"""

        self.ui_utils.clear_screen()
        cabincrews = self.logic_wrapper.get_all_cabincrews()
        print("[ALL CABIN CREW]\n")
        for index, cabincrew in enumerate(cabincrews):
            print(f"{index + 1:>2}.{' Name: ':^2}{cabincrew.name:<}, {'Role: '}{cabincrew.role}")
        input("\nPress [ENTER] to exit: ")
