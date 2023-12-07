from logic.logic_wrapper import LogicWrapper
from ui.register_employee_ui import RegisterEmployeeUI
from model.employee import Employee

from utils.ui_utils import UIUtils

class PilotUI:
    def __init__(self, wrapper) -> None:
       self.logic_wrapper = wrapper
       self.ui_utils = UIUtils()
       self.input_str = "Enter your choice: "

    def menu_output(self):
        self.ui_utils.clear_screen()
        print(f"[PILOTS]\n")
        print(f"1. Register pilot")
        print(f"2. List All pilots")
        print(f"3. View specific pilot")
        print(f"4. View All Captain Pilots")
        print(f"5. View All Co-Pilots")
        print(f"\n[B]ack")

    def input_prompt(self):
        """ Takes in input from user """
        while True:
            self.menu_output()
            user_input = input("\n" + self.input_str).lower()
            if user_input == "b":
                break

            elif user_input == "1":
                register_employee_menu = RegisterEmployeeUI(self.logic_wrapper)
                e = Employee()
                register_employee_menu.register_pilot(e)   

            elif user_input == "2":
                self.ui_utils.clear_screen()
                pilots = self.logic_wrapper.get_all_pilots()
                print("[ALL PILOTS]\n")
                for index, pilot in enumerate(pilots):
                    print(f"{index+1:>2}.{' name: ':^2}{pilot.name:<}, {'Role: '}{pilot.role}")
                input("\nPress [ENTER] to exit: ")

            elif user_input == "3":
                self.ui_utils.clear_screen()

                license_types = {
                    "1": "NAFokkerF28",
                    "2": "NAFokkerF100",
                    "3": "NABAE146"
                }
                print("[Pilot(s) List by License]\n")

                while True:
                    print("1. NAFokkerF28 2. NAFokkerF100 3. NABAE146")
                    license_type_input = input("\nEnter License Type (1, 2, 3 or b): ")
                    if license_type_input in license_types:
                        license_type_input = license_types[license_type_input]
                        break
                    else:
                        print("Invalid input. Please enter 1, 2, or 3.")

                print(f"\nShowing pilot(s) for {license_type_input}\n")
                print(self.logic_wrapper.get_all_pilots_by_license(license_type_input))
                input("\nPress [ENTER] to exit: ")

            elif user_input == "4":
                self.ui_utils.clear_screen()
                captains = self.logic_wrapper.get_all_captain_pilots()
                print("[ALL CAPTAIN PILOTS]\n")
                for index, captain in enumerate(captains):
                    print(f"{index+1:>2}. {captain}")
                input("\nPress [ENTER] to exit: ")

            elif user_input == "5":
                self.ui_utils.clear_screen()
                copilots = self.logic_wrapper.get_all_copilots()
                print("[ALL COPILOTS]\n")
                for index, copilot in enumerate(copilots):
                    print(f"{index+1:>2}. {copilot}")
                input("\nPress [ENTER] to exit: ")
            # else:
            #     self.input_str = "Invaild. Enter another choice: "

