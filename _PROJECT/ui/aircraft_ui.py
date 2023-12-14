from logic.logic_wrapper import LogicWrapper
from model.aircraft import Aircraft
from utils.ui_utils import UIUtils

DASH_AMOUNT = 46

class AircraftUI:
    def __init__(self, wrapper) -> None:
        self.logic_wrapper = wrapper
        self.ui_utils = UIUtils()
        self.input_prompt_str = "Enter you choice: "


    def menu_output(self) -> None:
        """Prints out the options for the Aircraft UI"""
        header = "[AIRCARFT]"
        self.ui_utils.clear_screen()
        print(header + "-" * (DASH_AMOUNT - len(header)) + "\n")
        print("\n" * 5)
        print(f"\t1. View All Aircrafts\n")
        print("\n" * 5)
        print(f"\t\t\t\t\t[B]ack")
        print("-" * DASH_AMOUNT)

    def input_prompt(self) -> None:
        """Takes in an input from user, and jumpst to a specific UI/function based on that input."""

        user_input = ""

        while user_input != "b":
            self.menu_output()
            user_input = input("\n" + self.input_prompt_str).lower()

            if user_input == "1":
                self.list_all_aircarfts()
            else:
                self.input_prompt_str = "\033[31mInvalid\033[0m. Enter another choice: "


    def list_all_aircarfts(self):
        """Lists all aircrafts from the aircraft.csv file"""
        header = "[ALL AIRCRAFTS]"
        self.ui_utils.clear_screen()
        aircrafts = self.logic_wrapper.get_all_aircrafts()
        print(header + "-" * (DASH_AMOUNT - len(header)))
        print("\n" * 3)
        for aircraft in (aircrafts):
            print(f"{aircraft.plane_insignia} {'PTI: '}{aircraft.plane_type_id:<15} {'DOM: '}{aircraft.date_of_manufacture:>4}, {'Last Maintenance: '}{aircraft.last_maintenance:>4}")
        print("\n" * 2)
        print("-" * DASH_AMOUNT)
        input("\nPress \033[34m[ENTER]\033[0m to exit: ")