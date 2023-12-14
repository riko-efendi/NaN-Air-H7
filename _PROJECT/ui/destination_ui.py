from logic.logic_wrapper import LogicWrapper
from model.destination import Destination

from utils.ui_utils import UIUtils

DASH_AMOUNT = 46

class DestinationUI:
    def __init__(self, logic_connection:LogicWrapper) -> None:
        self.logic_wrapper = logic_connection
        self.ui_utils = UIUtils()
        self.input_prompt_str = "Enter your choice: "


    def menu_output(self):
        """Prints out the options for the Destination UI"""
        header = "[Destination]"
        self.ui_utils.clear_screen()
        print(header + "-" * (DASH_AMOUNT - len(header)) + "\n")
        print("\n" * 4)
        print(f"\t1. Register Destination\n")
        print(f"\t2. View All Destinations\n")
        print("\n" * 4)
        print(f"\t\t\t\t\t[B]ack")
        print("-" * DASH_AMOUNT)


    def input_prompt(self):
        """Takes in an input from user, and jumpst to a specific UI/function based on that input."""
        
        user_input = ""

        while user_input != "b":
            self.menu_output()
            user_input = input("\n" + self.input_prompt_str).lower()

            if user_input == "1":
                self.register_destination()
            elif user_input == "2":
                self.list_all_destinations()
            else:
                self.input_prompt_str = "Invalid. Enter another choice: "


    def register_destination(self):
        """Creates an instance of a destination and then registers it in the destinations.csv file"""
        header = "[Register Destination]"
        self.ui_utils.clear_screen()
        d = Destination()

        print(header + "-" * (DASH_AMOUNT - len(header)) + "\n")
        print("\n" * 4)
        d.id = input("Enter destination three letter id: ").upper()         # Needs error handling
        d.destination = input("Enter destination name: ").capitalize()
        d.numeric_id = input("Enter destination numeric id: ")
        d.flight_time_from_kef = input("Enter flight time in hrs, from KEF airport: ")
        self.logic_wrapper.register_destination(d)
        print(f"\n{d.destination} is successfully created.")
        input("\nPress \033[34m[ENTER]\033[0m to exit: ")


    def list_all_destinations(self):
        """Lists all destinations in destinations.csv file"""
        header = "[All Destinations]"
        self.ui_utils.clear_screen()
        destinations = self.logic_wrapper.get_all_destinations()

        print(header + "-" * (DASH_AMOUNT - len(header)) + "\n")
        print("\n" * 2)
        for destination in (destinations):
            print(f"{destination.destination:^20} {destination.id:>15} {destination.numeric_id}")
        print("\n" * 2)
        print("-" * DASH_AMOUNT)
        input("\nPress \033[34m[ENTER]\033[0m to exit: ")
