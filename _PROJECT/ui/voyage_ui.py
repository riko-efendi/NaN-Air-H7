from logic.logic_wrapper import LogicWrapper
from ui.destination_ui import DestinationUI
from ui.aircraft_ui import AircraftUI
from ui.flights_ui import FlightsUI
from ui.edit_voyage_ui import EditVoyageUI
from ui.voyage_list_ui import VoyageListUI
from model.voyage import Voyage
from utils.ui_utils import UIUtils
from utils.ascii_art import AsciiArt

DASH_AMOUNT = 38
SPACING = " " * int((DASH_AMOUNT -10)/2)
LOGO_SPACING = " " * int((DASH_AMOUNT -10)/4)

class VoyageUI:
    def __init__(self, logic_connection:LogicWrapper) -> None:
        self.ui_utils = UIUtils()
        self.logic_wrapper = logic_connection
        self.input_prompt_str = "Enter your choice: "
        self.ascii_art = AsciiArt()

    def menu_output(self) -> None:
        """Prints out the options for the Voyage UI"""

        header = "[VOYAGE]"
        self.ui_utils.clear_screen()
        print(self.ascii_art.nanair_logo(LOGO_SPACING))
        print(header + "-" * (DASH_AMOUNT - len(header)) +"\n")
        print(f"{SPACING}1. Create Voyage\n")
        print(f"{SPACING}2. List Voyages\n")
        print(f"{SPACING}3. Edit Voyage\n")
        print(f"{SPACING}4. Destination\n")
        print(f"{SPACING}5. Flights\n")
        print(f"{SPACING}6. Aircraft")
        print(f"{' ' * (DASH_AMOUNT - len('[B]ack'))}[B]ack")
        print("-"*DASH_AMOUNT)

    def input_prompt(self) -> None:
        """Takes in an input from user, and jumpst to a specific UI/function based on that input."""

        user_input = ""

        while user_input != "b":
            self.menu_output()
            user_input = input(self.input_prompt_str).lower()

            if user_input == "1":
                create_coyage_menu = EditVoyageUI(self.logic_wrapper)
                create_coyage_menu.create_voyage()

            elif user_input =="2":
                voyage_list_ui = VoyageListUI(self.logic_wrapper)
                voyage_list_ui.input_prompt()

            elif user_input =="3":
                voyage_list_ui = EditVoyageUI(self.logic_wrapper)
                voyage_list_ui.edit_voyage()

            elif user_input == "4":
                destination_menu = DestinationUI(self.logic_wrapper)
                destination_menu.input_prompt()

            elif user_input == "5":
                flights_menu = FlightsUI(self.logic_wrapper)
                flights_menu.input_prompt()

            elif user_input == "6":
                aircraft_menu = AircraftUI(self.logic_wrapper)
                aircraft_menu.input_prompt()

            else:
                self.input_prompt_str = "Invalid. Enter another choice: "
            
            self.input_prompt_str = "Enter your choice: "
