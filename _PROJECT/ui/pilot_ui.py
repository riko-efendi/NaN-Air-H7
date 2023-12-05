from logic.logic_wrapper import LogicWrapper
from ui.register_employee_ui import RegisterEmployeeUI
from model.employee import Employee
from utils.ui_utils import UIUtils

class PilotUI:
    def __init__(self, wrapper) -> None:
       self.logic_wrapper = LogicWrapper()
       self.ui_utils = UIUtils()

    def menu_output(self):

        options = "1. Register Pilot\n2. List All Pilots\n3. View Specific Pilot\n\n[B]ack"
        boarder = self.ui_utils.get_boarder("[PILOTS MENU]", options, 0, 5)
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
                register_employee_menu.register_pilot(e)   

            elif user_input == "2":
                pilots = self.logic_wrapper.get_all_pilots()
                self.ui_utils.clear_screen()
                print("[All Pilots]\n")
                for index, pilot in enumerate(pilots):
                    print(f"{index+1:>2}.{' name: ':^2}{pilot.name:<}, {'Role: '}{pilot.role}")
                input("\nPress ENTER to exit: ")

