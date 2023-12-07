from logic.logic_wrapper import LogicWrapper
from model.destination import Destination

from utils.ui_utils import UIUtils

class DestinationUI:
    def __init__(self, wrapper) -> None:
        self.logic_wrapper = wrapper
        self.ui_utils = UIUtils()
        self.input_str = "Enter your choice: "


    def menu_output(self):
        """Takes in an input from user, and jumpst to a specific UI/function based on that input."""

        self.ui_utils.clear_screen()
        print(f"[DESTINATION]\n")
        print(f"1. Register Destination")
        print(f"2. List all Destinations")
        print(f"\n[B]ack")


    def input_prompt(self):
        """Takes in an input from user, and jumpst to a specific UI/function based on that input."""
        
        user_input = ""

        while user_input != "b":
            self.menu_output()
            user_input = input("\n" + self.input_str).lower()

            if user_input == "1":
                self.register_destination()
            elif user_input == "2":
                self.list_all_destinations()
            else:
                self.input_str = "Invalid. Enter another choice: "


    def register_destination(self):
        """Creates an instance of a destination and then registers it in the destinations.csv file"""

        self.ui_utils.clear_screen()
        d = Destination()

        print("[REGISTER DESTINATION]\n")
        d.id = input("Enter destination three letter id: ").upper()         # Needs error handling
        d.destination = input("Enter destination name: ").capitalize()
        d.numeric_id = input("Enter destination numeric id: ")
        self.logic_wrapper.create_destination(d)
        print(f"\n{d.destination} is successfully created.")
        input("\nPress [ENTER] to exit: ")


    def list_all_destinations(self):
        """Lists all destinations in destinations.csv file"""

        self.ui_utils.clear_screen()
        destinations = self.logic_wrapper.get_all_destinations()

        print("[All DESTINATIONS]\n")
        for index, destination in enumerate(destinations):
            print(f"{index+1:>2}.{' name: ':^2}{destination.destination:<}, {'id: '}{destination.id}, {destination.numeric_id}")
        input("\nPress [ENTER] to exit: ")
