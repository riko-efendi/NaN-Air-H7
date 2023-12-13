from logic.logic_wrapper import LogicWrapper
from model.destination import Destination
from utils.ui_utils import UIUtils

from ui.input_validation import *


class DestinationUI:
    def __init__(self, logic_connection:LogicWrapper) -> None:
        self.logic_wrapper = logic_connection
        self.ui_utils = UIUtils()
        self.input_prompt_str = "Enter your choice: "


    def menu_output(self):
        """Prints out the options for the Destination UI"""

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
            user_input = input("\n" + self.input_prompt_str).lower()

            if user_input == "1":
                self.register_destination()
            elif user_input == "2":
                self.list_all_destinations()
            else:
                self.input_prompt_str = "Invalid. Enter another choice: "


    def register_destination(self):
        """Creates an instance of a destination and then registers it in the destinations.csv file"""

        self.ui_utils.clear_screen()
        d = Destination()
        header = "[REGISTER DESTINATION]"
        self.ui_utils.print_destination(d, header)
        
        while True:
            try:
                d.id = input("Enter destination three letter id: ").upper()
                validate_id(d.id)
                self.ui_utils.print_destination(d, header)
                break

            except LengthERROR:
                self.ui_utils.print_destination(d, header)
                print("Length error. Please enter 3 letter id")
            except ValueError:
                self.ui_utils.print_destination(d, header)
                print("Invalid value. Please enter letters only")
                
        while True:
            try:
                d.destination = input("Enter destination name: ").capitalize()
                validate_name_destination(d.destination)
                self.ui_utils.print_destination(d, header)
                break

            except LengthERROR:
                self.ui_utils.print_destination(d, header)
                print("Length error. Please enter a valid destination.")
            except ValueError:
                self.ui_utils.print_destination(d, header)
                print("Invalid value. Please enter letters only.")

        while True:
            try:
                d.numeric_id = input("Enter destination numeric id: ")
                validate_numeric_id(d.numeric_id)
                self.ui_utils.print_destination(d, header)
                break

            except LengthERROR:
                self.ui_utils.print_destination(d, header)
                print("Invalid length. Please enter 4 digit id.")
            except ValueError:
                self.ui_utils.print_destination(d, header)
                print("invalid value. Please enter only digits.")

        while True:
            try:
                d.flight_time_from_kef = input("Enter flight time in hrs, from KEF airport: ")
                validate_flight_time(d.flight_time_from_kef)
                self.ui_utils.print_destination(d, header)
                break

            except LengthERROR:
                self.ui_utils.print_destination(d, header)
                print("Flight time exceeded. Please enter a valid flight time.")
            except ValueError:
                self.ui_utils.print_destination(d, header)
                print("Invalid Value. Please enter only digits.")

        self.logic_wrapper.register_destination(d)
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
