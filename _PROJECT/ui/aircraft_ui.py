from logic.aircraft_logic import Aircraft
from model.aircraft import Aircraft
from utils.utils import UIUtils

class AircraftUI:
    def __init__(self, wrapper) -> None:
        self.logic_wrapper = wrapper

    def menu_output(self):
        header = f"[Aircraft]"

        print()
        print(header)
        print()
        print(f"1. Register aircraft")
        print(f"2. List all aircrafts")
        print(f"q. Quit")

    def input_prompt(self):
        """This takes the input of the user"""
        while True:
            self.menu_output()
            user_input = input("\nEnter your choice: ").lower()
            if user_input == "q":
                print("Quitting")
                break
            elif user_input == "1":
                pass
            elif user_input == "2":
                aircrafts = self.logic_wrapper.get_all_aircrafts()
                print()
                print()
                print()
                for index, aircrafts in enumerate(aircrafts):
                    print(f"{index+1:>2}.{' sign ':^2}{aircrafts.sign},{aircrafts.id},{aircrafts.manufacture},{aircrafts.maintinance}")
            else:
                print("Invalid")