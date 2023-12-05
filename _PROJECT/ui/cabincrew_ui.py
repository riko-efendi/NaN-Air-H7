from logic.logic_wrapper import LogicWrapper
from model.employee import Employee
from ui.register_employee_ui import RegisterEmployeeUI
from utils.ui_utils import UIUtils


class CabinCrewUI:
    def __init__(self, wrapper) -> None:
       self.logic_wrapper = LogicWrapper()
       self.ui_utils = UIUtils()

    def menu_output(self):

        options = "1. Register Cabin Crew\n2. List All Cabin Crew\n3. View Specific Cabin Crew\n\n[B]ack"
        boarder = self.ui_utils.get_boarder("[CABIN CREW]", options, 0, 5)
        self.ui_utils.clear_screen()
        print(boarder)

    def input_prompt(self):
        """ Takes in input from user """
        while True:
            self.menu_output()
            user_input = input("Enter your choice: ").lower()
            if user_input == "b":
                break

            elif user_input == "1":
                register_employee_menu = RegisterEmployeeUI(self.logic_wrapper)
                e = Employee()
                register_employee_menu.register_cabin_crew(e)   

            elif user_input == "2":
                self.ui_utils.clear_screen()
                cabincrews = self.logic_wrapper.get_all_cabincrews()
                print("[All CABIN CREW]\n")
                for index, cabincrew in enumerate(cabincrews):
                    print(f"{index+1:>2}.{' Name: ':^2}{cabincrew.name:<}, {'Role: '}{cabincrew.role}")
                input("\nPress any key to exit: ")