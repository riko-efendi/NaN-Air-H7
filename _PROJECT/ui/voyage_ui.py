from logic.logic_wrapper import LogicWrapper
from ui.destination_ui import DestinationUI
from ui.all_lists_UI import List
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
        print(f"q. Quit")

    def input_prompt(self):
        while True:
            self.menu_output()
            user_input = input("\nEnter your choice: ").lower()
            if user_input == "q":
                print("Quitting")
                break
            elif user_input == "2":
                file_name = "_PROJECT/files/destinations.csv"
                list_instance = List(file_name)
                

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
