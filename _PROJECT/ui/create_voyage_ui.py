from utils.ui_utils import UIUtils
from ui.destination_ui import DestinationUI
from model.flight import Flight
from datetime import datetime, timedelta
from logic.logic_wrapper import LogicWrapper


class CreateVoyageUI:
    def __init__(self, logic_connection:LogicWrapper) -> None:
        self.ui_utils = UIUtils()
        self.logic_wrapper = logic_connection
        self.destination_ui = DestinationUI(self.logic_wrapper)
        self.input_prompt_str = "Enter your choice: "
        flight_1_nr = self.logic_wrapper.generate_flight_nr()
        flight_2_nr = self.logic_wrapper.generate_flight_nr()

        while flight_2_nr == flight_1_nr:
            # Just so these two flight numbers won't be the same
            flight_2_nr = self.logic_wrapper.generate_flight_nr()

        self.flight_1 = Flight(flight_nr=flight_1_nr, dep_from="KEF")
        self.flight_2 = Flight(flight_nr=flight_2_nr, arr_at="KEF")



    def input_prompt(self) -> None:
        """Takes in an input from user, and jumpst to a specific UI/function based on that input."""

   
        self.assign_destination()
        self.assign_times(self.flight_1)
        self.assign_times(self.flight_2)
            

    def assign_destination(self):
        "Window to select which destination you want to assign to a voyage"

        destinations_dict = self.logic_wrapper.get_all_destinations(False, True)
        user_input = ""

        while user_input != "c":
            self.print_destinations(destinations_dict)
            user_input = input("\n" + self.input_prompt_str).lower()

            if user_input == "m":
                self.destination_ui.register_destination()
                destinations_dict = self.logic_wrapper.get_all_destinations(False, True) # Update destination_dict after adding a new element
            else:
                try: 
                    if int(user_input) - 1 in destinations_dict:
                        self.flight_1.arr_at = destinations_dict[int(user_input) - 1].id
                        self.flight_1.duration = destinations_dict[int(user_input) - 1].flight_time_from_kef

                        self.flight_2.dep_from = destinations_dict[int(user_input) - 1].id
                        self.flight_2.duration = destinations_dict[int(user_input) - 1].flight_time_from_kef
                        return True
                    
                except ValueError:
                    self.input_prompt_str = "Invalid. Choose again: " # Needs error handling for values that go beyond
        return False


    def print_destinations(self, destinations):
        """Prints destinations from a dictionary"""

        self.ui_utils.clear_screen()
        print(f"[ASSIGN DESTINATION TO VOYAGE]\n")
        for index, destination in destinations.items():
            print(f"{index + 1}. {destination.id}")
        
        print(f"\n[C]ancel\t[M]ake new Destination")


    def assign_times(self, flight:Flight) -> None:

        self.ui_utils.clear_screen()
        print(f"[SELECT DESTINATION]\n")
        #dep_date = input(f"At what date do you want to depart from {flight.dep_from}? (YYYY-MM-DD)")
        dep_date = "2023-12-31"
        #dep_time = input(f"When do you want to depart from {flight.dep_from}? (HH:MM:SS) ")
        dep_time = "23:59:00"
        dep_datetime = dep_date + " " + dep_time

        flight.dep = dep_datetime
        flight.arr = self.add_hours_to_datetime(dep_datetime, flight.duration)


        

    def add_hours_to_datetime(self, datetime_str, hours_to_add):
        datetime_format = "%Y-%m-%d %H:%M:%S"
        
        original_datetime = datetime.strptime(datetime_str, datetime_format)
        new_datetime = original_datetime + timedelta(hours=int(hours_to_add))
        new_datetime_str = new_datetime.strftime("%Y-%m-%d %H:%M:%S")

        return new_datetime_str




        



