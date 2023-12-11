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

        # 2 Flight classes created, combined they make a single voyage.
        flight_1_nr = self.logic_wrapper.generate_flight_nr()
        flight_2_nr = self.logic_wrapper.generate_flight_nr()

        # At the offchance of them being handed the same flight_nr
        while flight_2_nr == flight_1_nr:
            flight_2_nr = self.logic_wrapper.generate_flight_nr()

        self.flight_1 = Flight(flight_nr=flight_1_nr, dep_from="KEF")
        self.flight_2 = Flight(flight_nr=flight_2_nr, arr_at="KEF")



    def input_prompt(self) -> None:
        """Takes in an input from user, and jumpst to a specific UI/function based on that input."""
   
        self.assign_destination()
        self.assign_times(self.flight_1)
        self.assign_times(self.flight_2)
        self.logic_wrapper.register_flight(self.flight_1)
        self.logic_wrapper.register_flight(self.flight_2)

        input("Voyage succesfully created. Press [ENTER] to exit: ")
            

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
        """Assign date and time in the correct format to a flight"""

        self.print_flight_info(flight)
        dep_date = input(f"\nAt what date do you want to depart from {flight.dep_from}? (YYYY-MM-DD)")
        dep_time = input(f"\nWhen do you want to depart from {flight.dep_from}? (HH:MM:SS) ")
        dep_datetime = dep_date + " " + dep_time
        flight.dep = dep_datetime
        flight.arr = self.add_hours_to_datetime(dep_datetime, str(flight.duration))
        self.print_flight_info(flight)
        input("\nPress [ENTER] to exit: ")


    def add_hours_to_datetime(self, datetime_str, hours_to_add):
        """Adds the durations of the flight to the departing time"""

        datetime_format = "%Y-%m-%d %H:%M:%S"
        original_datetime = datetime.strptime(datetime_str, datetime_format)
        new_datetime = original_datetime + timedelta(hours=int(hours_to_add))
        new_datetime_str = new_datetime.strftime("%Y-%m-%d %H:%M:%S")

        return new_datetime_str
    
    def print_flight_info(self, flight:Flight):
        """Prints out for user info on current flight"""

        self.ui_utils.clear_screen()
        print(f"[ASSIGN DATE AND TIME]\n")
        print(f"Departing Destination: {flight.dep_from}")
        print(f"Arriving Destination: {flight.arr_at}")
        print(f"Time of Departure: {flight.dep}")
        print(f"Time of Arrival: {flight.arr}")





        



