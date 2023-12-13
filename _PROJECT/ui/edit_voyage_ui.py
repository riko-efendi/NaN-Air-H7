from utils.ui_utils import UIUtils
from ui.destination_ui import DestinationUI
from ui.voyage_list_ui import VoyageListUI
from model.voyage import Voyage
from model.flight import Flight
from model.destination import Destination
from datetime import datetime, timedelta
from logic.logic_wrapper import LogicWrapper


class EditVoyageUI:
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


    def create_voyage(self) -> None:
        """Takes in an input from user, and jumpst to a specific UI/function based on that input."""
   
        # Use this as a break statement
        if not self.assign_destination():
            return None
        # Use this as a break statement
        if not self.assign_times(self.flight_1):
            return None
        input("\nPress [ENTER] to confirm: ")
        # Use this as a break statement
        if not self.assign_times(self.flight_2):
            return None
        
        user_input = input("\nDo you want to assign Crew now?: (Y/N)").lower()

        if user_input =="y":
            self.assign_crew(self.flight_1, self.flight_2)

        # Create a list with the created voyge to put into the  print voyages function
        created_voyage = [Voyage(self.flight_1, self.flight_2)]

        self.ui_utils.print_voyages(created_voyage, "[CREATED VOYAGE]")
        input("Voyage succesfully created. Press [ENTER] to exit: ")

        self.logic_wrapper.register_flight(self.flight_1)
        self.logic_wrapper.register_flight(self.flight_2)


    def assign_crew(self, flight_1:Flight, flight_2:Flight):
        """Assignes crew to a voyage"""

        captain = self.print_available_crew(flight_1.depart_date, flight_2.arr_date, "Pilot", "Captain")
        copilot = self.print_available_crew(flight_1.depart_date, flight_2.arr_date, "Pilot", "Copilot")

        fsm = self.print_available_crew(flight_1.depart_date, flight_2.arr_date, "Cabincrew", "Flight Service Manager")
        fa1 = self.print_available_crew(flight_1.depart_date, flight_2.arr_date, "Cabincrew", "Flight Attendant")
        fa2 = self.print_available_crew(flight_1.depart_date, flight_2.arr_date, "Cabincrew", "Flight Attendant")

        flight_1.captain = captain
        flight_2.captain = captain
    
        flight_1.copilot = copilot        
        flight_2.copilot = copilot

        flight_1.fsm = fsm
        flight_2.fsm = fsm

        flight_1.fa1 = fa1
        flight_2.fa1 = fa1

        flight_1.fa2 = fa2
        flight_2.fa2 = fa2


    def edit_voyage(self):
        """User selects a voyage to assign new crew to"""

        voyages = self.logic_wrapper.get_upcoming_voyages()
        self.ui_utils.print_voyages(voyages, "[EDIT VOYAGE]")
        user_input = input("Select Voyage to edit: ")
        voyage = voyages[int(user_input) - 1]
        self.assign_crew(voyage.flight_1, voyage.flight_2)
        self.logic_wrapper.update_voyage(voyage)


    def assign_destination(self) -> bool:
        """Window to select which destination you want to assign to a voyage"""

        destinations_dict = self.logic_wrapper.get_all_destinations(False, True)
        input_prompt_str = "Enter your choice: "
        user_input = ""

        while user_input != "c":
            self.print_destinations(destinations_dict)
            user_input = input("\n" + input_prompt_str).lower()

            if user_input == "m":
                # Open the register destination window
                self.destination_ui.register_destination()

                # Update the destination dictionary
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
                    input_prompt_str = "Invalid. Choose again: " # Needs error handling for values that go beyond
        return False


    def assign_times(self, flight:Flight) -> bool:
        """Assign date and time in the correct format to a flight"""

        # Update flight info
        self.print_flight_info(flight)
        dep_date = input(f"\nAt what date do you want to depart from {flight.dep_from}? (YYYY-MM-DD): ").lower() # Needs Error handling

        if dep_date == "c":
            return False
        
        flight.depart_date = dep_date

        #Update flight info
        self.print_flight_info(flight)
        dep_time = input(f"\nAt what time do you want to depart from {flight.dep_from}? (HH:MM:SS): ").lower() # Needs error handling

        if dep_time == "c":
            return False

        # Add the date and time togheter to work as a single variable when going into the add hours function
        dep_datetime = dep_date + " " + dep_time
        flight.depart_time = dep_time
        flight.arr_date, flight.arr_time = self.add_hours_to_datetime(dep_datetime, str(flight.duration))

        # Update flight info 
        self.print_flight_info(flight)

        return True


    def add_hours_to_datetime(self, datetime_str, hours_to_add): # This might need to be in the logic layer
        """Adds the durations of the flight to the departing time"""

        datetime_format = "%Y-%m-%d %H:%M:%S"
        original_datetime = datetime.strptime(datetime_str, datetime_format)
        new_datetime = original_datetime + timedelta(hours=int(hours_to_add))
        new_datetime_str = new_datetime.strftime("%Y-%m-%d %H:%M:%S")

        return new_datetime_str.split(" ")
    

    def print_available_crew(self, dep_date, arr_date, role, rank):
        """Print available crew, by inputed date range and the role and rank of the employee. Returns the kennitala of a selected Employee"""

        employees = self.logic_wrapper.get_available_employees(dep_date, arr_date, role, rank)
        self.ui_utils.clear_screen()
        print(f"[SELECT {rank.upper()}]\n")
        for index, employee in enumerate(employees):
            print(f"{index + 1}. {employee.name}") 
        user_input = input("\nEnter your choice: ")

        return employees[int(user_input) - 1].kennitala
    

    def print_flight_info(self, flight:Flight) -> None:
        """Prints out for user info on current flight"""

        self.ui_utils.clear_screen()
        print(f"[ASSIGN DATE AND TIME]\n")
        print(f"Departing Destination: {flight.dep_from}")
        print(f"Arriving Destination: {flight.arr_at}")
        print(f"Date of Departure: {flight.depart_date}")
        print(f"Time of Departure: {flight.depart_time}")
        print(f"Date of Arrival: {flight.arr_date}")
        print(f"Time of Arrival: {flight.arr_time}")
        print(f"\n[C]ancel")
    

    def print_destinations(self, destinations:dict) -> None:
        """Prints destinations from a dictionary"""

        self.ui_utils.clear_screen()
        print(f"[ASSIGN DESTINATION TO VOYAGE]\n")
        for index, destination in destinations.items():
            print(f"{index + 1}. {destination.id}. Flight Time from KEF: {destination.flight_time_from_kef} hrs")
        
        print(f"\n[C]ancel\t[M]ake new Destination")