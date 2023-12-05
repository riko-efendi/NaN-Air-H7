from logic.logic_wrapper import LogicWrapper
from model.destination import Destination

class DestinationUI:
    def __init__(self, wrapper) -> None:
        self.logic_wrapper = wrapper

    def menu_output(self):
        header = f"[Destination]"

        print()
        print(header)
        print()
        print(f"1. Register Destination")
        print(f"2. List all destinations")
        print(f"q. Quit")

    def input_prompt(self):
        while True:
            self.menu_output()
            user_input = input("\nEnter your choice: ").lower()
            if user_input == "q":
                print("Quitting")
                break
            elif user_input == "1":
                d = Destination()
                print()
                print("[Create a New Destination]")
                print()
                d.id = input("Enter new destination's id: ")
                d.destination = input("Enter destination's name: ")
                d.numeric_id = input("Enter destination's numeric id: ")
                self.logic_wrapper.create_destination(d)
                print(f"\n{d.destination} is successfully created.")
            elif user_input == "2":
                destinations = self.logic_wrapper.get_all_destinations()
                print()
                print("[All Destinations]")
                print()
                for index, destination in enumerate(destinations):
                    print(f"{index+1:>2}.{' name: ':^2}{destination.destination:<}, {'id: '}{destination.id}, {destination.numeric_id}")
            else:
                print("Invalid")