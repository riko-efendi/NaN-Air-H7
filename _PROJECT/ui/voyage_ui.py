from ui.destination_ui import DestinationUI
from ui.aircraft_ui import AircraftUI
from ui.flights_ui import FlightsUI
from ui.create_voyage_ui import CreateVoyageUI
from model.voyage import Voyage

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
        print(f"2. List Voyage")
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
            elif user_input == "1":
                voyage_menu = CreateVoyageUI(self.logic_wrapper)
                e = Voyage()
                voyage_menu.create_voyage(e)


            elif user_input == "3":
                destination_menu = DestinationUI(self.logic_wrapper)
                back_method = destination_menu.input_prompt()
                if back_method == "q":
                    return "q"
                pass

            elif user_input == "4":
                flights_menu = FlightsUI(self.logic_wrapper)
                back_method = flights_menu.input_prompt()

            elif user_input == "5":
                aircraft_menu = AircraftUI(self.logic_wrapper)
                back_method = aircraft_menu.input_prompt()
                if back_method == "q":
                    return "q"
                pass

            else:
                self.input_string = "Invalid. Enter another choice: "
