from logic.logic_wrapper import LogicWrapper
from ui.destination_ui import DestinationUI
from ui.aircraft_ui import AircraftUI
#from funclibrary.functions import clear_screen


class VoyageUI:
    def __init__(self, wrapper) -> None:
        self.logic_wrapper = wrapper

    def menu_output(self):
        header = f"[VOYAGE]"
        
        print()
        print(header)
        print()
        print(f"1. Create Voyage")
        print(f"2. List Voyage")
        print(f"3. Destination")
        print(f"4. Flight")
        print(f"5. Aircraft")
        print(f"\n[B]ack")


    def input_prompt(self):
        while True:
            self.menu_output()
            user_input = input("\nEnter your choice: ").lower()
            if user_input == "b":
                break
            elif user_input == "3":
                destination_menu = DestinationUI(self.logic_wrapper)
                back_method = destination_menu.input_prompt()
                if back_method == "q":
                    return "q"
                pass
            elif user_input == "5":
                aircraft_menu = AircraftUI(self.logic_wrapper)
                back_method = aircraft_menu.input_prompt()
                if back_method == "q":
                    return "q"
                pass
            else:
                print("Invalid")
