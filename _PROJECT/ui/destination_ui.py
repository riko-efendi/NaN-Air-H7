from logic.logic_wrapper import LogicWrapper
from model.destination import Destination

from utils.ui_utils import UIUtils

class DestinationUI:
    def __init__(self, wrapper) -> None:
        self.logic_wrapper = wrapper
        self.ui_utils = UIUtils()
        self.input_str = "Enter your choice: "

    def menu_output(self):
        self.ui_utils.clear_screen()
        print(f"[Destination]\n")
        print(f"1. Register Destination")
        print(f"2. List all destinations")
        print(f"\n[B]ack")

    def input_prompt(self):
        while True:
            self.menu_output()
            user_input = input("\n" + self.input_str).lower()

            if user_input == "b":
                break

            elif user_input == "1":
                d = Destination()
                self.ui_utils.clear_screen()
                print("[Create a New Destination]\n")
                d.id = input("Enter new destination's id: ")
                d.destination = input("Enter destination's name: ")
                d.numeric_id = input("Enter destination's numeric id: ")
                self.logic_wrapper.create_destination(d)
                print(f"\n{d.destination} is successfully created.")
            
            elif user_input == "2":
                self.ui_utils.clear_screen()
                destinations = self.logic_wrapper.get_all_destinations()
                print("[All Destinations]\n")
                for index, destination in enumerate(destinations):
                    print(f"{index+1:>2}. {'id: '}{destination.id}, {destination.destination}, {destination.numeric_id}")
                input("\nPress [ENTER] to exit: ")
            else:
                self.input_str = "Invalid. Enter another choice: "