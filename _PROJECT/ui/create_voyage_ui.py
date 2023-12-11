<<<<<<< HEAD

from utils.ui_utils import UIUtils

class CreateVoyageUI():
    def __init__(self, wrapper) -> None:
        self.logic_wrapper = wrapper
        self.ui_utils = UIUtils()

    def create_voyage(self, voyage):
        """Creates a voyage"""
        self.ui_utils.clear_screen()
        print("\n[CREATE VOYAGE]\n")
        while True:
            flights = self.logic_wrapper.get_all_upcoming_flights()
            fid_list = [flight.flight_nr for flight in flights]

            while True: 
                #First we need a valid id for the first flight out(i need to somehow find a way as they
                # input the flight out code, there would be another individual list that are flights available to flight back in)
                voyage.flight_out = input("Input the flight out:")
                if voyage.flight_out in fid_list:
                    print("Valid ID!")
                    break
                else:
                    print("Please enter a valid ID.")
            #We iterate through the list of id (but i still need to somehow find the flights after 
            # they have inputed the first flight out. )
            while True:
                voyage.flight_in = input("Input the flight in:")
                if voyage.flight_in in fid_list:
                    print("Valid ID for flight in!")
                    break
                else:
                    print("Please enter a valid ID for flight in.")

            #if there was a pilot :) (This is optional)
            while True:

                find_pilot = input("Input the pilot: ")
                pilots = self.logic_wrapper.get_all_pilots()
                pilot_list = [pilot.name for pilot in pilots]
                
                if find_pilot in pilot_list or find_pilot == "":
                #then add this pilot to the csv file :) 
                    return
                else:
                    print("please enter a valid Pilot")








    



        #cabincrew = input("Input the cabin crew: ")

        
        #if cabincrew != None:
        

        #Add crew(optional?)
        #self.logic_wrapper.create_voyage()
        #print(f"\n{voyage.flight_out}-{voyage.flight_in} is successfully created.")
=======
from utils.ui_utils import UIUtils
from ui.destination_ui import DestinationUI
from model.flight import Flight
from model.destination import Destination
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



    def create_voyage(self) -> None:
        """Takes in an input from user, and jumpst to a specific UI/function based on that input."""
   
        if not self.assign_destination():
            return None
        if not self.assign_times(self.flight_1):
            return None
        input("\nPress [ENTER] to confirm: ")
        if not self.assign_times(self.flight_2):
            return None
        self.logic_wrapper.register_flight(self.flight_1)
        self.logic_wrapper.register_flight(self.flight_2)
        input("Voyage succesfully created. Press [ENTER] to exit: ")
            

    def assign_destination(self):
        "Window to select which destination you want to assign to a voyage"

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


    def print_destinations(self, destinations:dict) -> None:
        """Prints destinations from a dictionary"""

        self.ui_utils.clear_screen()
        print(f"[ASSIGN DESTINATION TO VOYAGE]\n")
        for index, destination in destinations.items():
            print(f"{index + 1}. {destination.id}. Flight Time from KEF: {destination.flight_time_from_kef} hrs")
        
        print(f"\n[C]ancel\t[M]ake new Destination")


    def assign_times(self, flight:Flight) -> None:
        """Assign date and time in the correct format to a flight"""

        # Update flight info
        self.print_flight_info(flight)
        dep_date = input(f"\nAt what date do you want to depart from {flight.dep_from}? (YYYY-MM-DD): ").lower()

        if dep_date == "c":
            return False
        
        flight.depart_date = dep_date

        #Update flight info
        self.print_flight_info(flight)
        dep_time = input(f"\nAt what time do you want to depart from {flight.dep_from}? (HH:MM:SS): ").lower()

        if dep_time == "c":
            return False

        # Add the date and time togheter to work as a single variable when going into the add hours function
        dep_datetime = dep_date + " " + dep_time
        flight.depart_time = dep_time
        flight.arr_date, flight.arr_time = self.add_hours_to_datetime(dep_datetime, str(flight.duration))

        # Update flight info 
        self.print_flight_info(flight)

        return True


    def add_hours_to_datetime(self, datetime_str, hours_to_add):
        """Adds the durations of the flight to the departing time"""

        datetime_format = "%Y-%m-%d %H:%M:%S"
        original_datetime = datetime.strptime(datetime_str, datetime_format)
        new_datetime = original_datetime + timedelta(hours=int(hours_to_add))
        new_datetime_str = new_datetime.strftime("%Y-%m-%d %H:%M:%S")

        return new_datetime_str.split(" ")
    
    def print_flight_info(self, flight:Flight):
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





        



>>>>>>> eead74ee80ec091cc353a879a80a68552811e54a
