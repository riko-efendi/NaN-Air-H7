from ui.destination_ui import DestinationUI
from ui.aircraft_ui import AircraftUI
from ui.flights_ui import FlightsUI
from utils.ui_utils import UIUtils


class VoyageUI:
    def __init__(self, logic_connection) -> None:
        self.ui_utils = UIUtils()
        self.logic_wrapper = logic_connection
        self.input_prompt_str = "Enter your choice: "

    def menu_output(self) -> None:
        """Prints out the options for the Voyage UI"""

        self.ui_utils.clear_screen()
        print(f"[VOYAGE]\n")
        print(f"1. Create Voyage")
        print(f"2. List Voyage")
        print(f"3. Destination")
        print(f"4. Flights")
        print(f"5. Aircraft")
        print(f"\n[B]ack")

    def input_prompt(self) -> None:
        """Takes in an input from user, and jumpst to a specific UI/function based on that input."""

        user_input = ""

        while user_input != "b":
            self.menu_output()
            user_input = input("\n" + self.input_prompt_str).lower()

            if user_input == "3":
                destination_menu = DestinationUI(self.logic_wrapper)
                destination_menu.input_prompt()

            elif user_input == "4":
                flights_menu = FlightsUI(self.logic_wrapper)
                flights_menu.input_prompt()

            elif user_input == "5":
                aircraft_menu = AircraftUI(self.logic_wrapper)
                aircraft_menu.input_prompt()

            else:
                self.input_prompt_str = "Invalid. Enter another choice: "
