from ui.destination_ui import DestinationUI
from ui.aircraft_ui import AircraftUI
from ui.flights_ui import FlightsUI

from utils.ui_utils import UIUtils



class VoyageUI:
    def __init__(self, logic_connection) -> None:
        self.ui_utils = UIUtils()
        self.logic_wrapper = logic_connection
        self.input_string = "Enter your choice: "

    def menu_output(self):
        self.ui_utils.clear_screen()
        print(f"[VOYAGE]\n")
        print(f"1. Create Voyage")
        print(f"2. List Past Voyages")
        print(f"3. Destination")
        print(f"4. Flights")
        print(f"5. Aircraft")
        print(f"\n[B]ack")

    def input_prompt(self):
        while True:
            self.menu_output()
            user_input = input("\n" + self.input_string).lower()
            if user_input == "q":
                print("Quitting")

            if user_input == "b":
                break

            elif user_input == "2":
                self.ui_utils.clear_screen()
                voyages = self.logic_wrapper.get_all_past_voyages()
                print("[ALL PAST VOYAGES]\n")

                for voyage in voyages:
                    print(voyage)
                input("\nPress [ENTER] to exit: ")

            elif user_input == "3":
                destination_menu = DestinationUI(self.logic_wrapper)
                destination_menu.input_prompt()

            elif user_input == "4":
                flights_menu = FlightsUI(self.logic_wrapper)
                flights_menu.input_prompt()

            elif user_input == "5":
                aircraft_menu = AircraftUI(self.logic_wrapper)
                aircraft_menu.input_prompt()

            else:
                self.input_string = "Invalid. Enter another choice: "

            



