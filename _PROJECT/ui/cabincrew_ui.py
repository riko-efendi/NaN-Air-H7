from logic.logic_wrapper import LogicWrapper
from model.employee import Employee
from ui.register_employee_ui import RegisterEmployeeUI

from utils.ui_utils import UIUtils

DASH_AMOUNT = 46

class CabinCrewUI:
    def __init__(self, wrapper) -> None:
       self.logic_wrapper = wrapper
       self.ui_utils = UIUtils()
       

    def menu_output(self) -> None:
        """Prints out the options for the Cabin Crew UI"""
        header = ("[CABIN CREW]")
        self.ui_utils.clear_screen()
        print(header + "-" * (DASH_AMOUNT - len(header)) + "\n")
        print(f"\t1. Register Cabin Crew\n")
        print(f"\t2. View All Cabin Crews\n")
        print(f"\t\t\t\t\t[B]ack")
        print("-" * DASH_AMOUNT)

    def input_prompt(self) -> None:
        """Takes in an input from user, and jumpst to a specific UI/function based on that input."""

        user_input = ""

        while user_input != "b":
            self.menu_output()
            user_input = input("\nEnter your choice: ").lower()

            if user_input == "1":
                self.register_cabin_crew()

            elif user_input == "2":
                self.list_all_cabin_crew()


    def register_cabin_crew(self) -> None:
        """Creates an employee and passes it to the Register Employee UI, where it is registered in the crew.csv file"""

        e = Employee(role="Cabincrew")
        register_employee_menu = RegisterEmployeeUI(self.logic_wrapper)
        register_employee_menu.register_employee(e, "[REGISTER CABIN CREW]")   

    def list_all_cabin_crew(self) -> None:
        """Prints out all cabin crew"""
        header = "[ALL CABIN CREWS]"
        self.ui_utils.clear_screen()
        cabincrews = self.logic_wrapper.get_all_cabincrews()
        print(header + "-" * (DASH_AMOUNT - len(header)) + "\n")
        for cabincrew in cabincrews:
            print(f"{cabincrew.name:^46}")
        print("\n"+ "-" * DASH_AMOUNT)
        input("\nPress \033[34m[ENTER]\033[0m to exit: ")
