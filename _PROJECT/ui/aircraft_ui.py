from logic.logic_wrapper import LogicWrapper
from model.aircraft import Aircraft
from utils.ui_utils import UIUtils

class AircraftUI:
    def __init__(self, wrapper) -> None:
        self.logic_wrapper = wrapper
        self.ui_utils = UIUtils()
        self.input_prompt_str = "Enter you choice: "


    def menu_output(self) -> None:
        """Prints out the options for the Aircraft UI"""

        self.ui_utils.clear_screen()
        print(f"[AIRCARFT]\n")
        print(f"1. Register aircraft")
        print(f"2. List all aircrafts")
        print(f"\n[B]ack")


    def input_prompt(self) -> None:
        """Takes in an input from user, and jumpst to a specific UI/function based on that input."""

        user_input = ""

        while user_input != "b":
            self.menu_output()
            user_input = input("\n" + self.input_prompt_str).lower()

            if user_input == "2":
                self.list_all_aircarfts()
            else:
                self.input_prompt_str = "Invalid. Enter another choice: "


    def list_all_aircarfts(self):
        """Lists all aircrafts from the aircraft.csv file"""


        self.ui_utils.clear_screen()
        aircrafts = self.logic_wrapper.get_all_aircrafts()
        print("[ALL AIRCRAFTS]\n")
        for index, aircraft in enumerate(aircrafts):
            print(f"{index+1:>2}. {'Plane Insignia':^2}{aircraft.plane_insignia:<}, {'Plane Type id: '}{aircraft.plane_type_id}, {'DOM: '}{aircraft.date_of_manufacture}, {'Last Maintenance: '}{aircraft.last_maintenance}")
        input("\nPress [ENTER] to exit: ")