from data.data_wrapper import DataWrapper
from utils.logic_utils import LogicUtils

from model.flight import Flight

import random

class FlightLogic:
    def __init__(self, data_connection:DataWrapper) -> None:
        self.data_wrapper = data_connection
        self.logic_utils = LogicUtils()

    def get_all_upcoming_flights(self):
        return self.inject_destinations_to_flight(self.data_wrapper.get_all_upcoming_flights())

    def get_all_past_flights(self):
        return self.inject_destinations_to_flight(self.data_wrapper.get_all_past_flights())

    def inject_destinations_to_flight(self, flights):
        destinations = self.data_wrapper.get_all_destinations()

        for flight in flights:
            for destination in destinations:
                if destination.id.strip() == flight.dep_from.strip():
                    flight.depart_dest = destination

                elif destination.id.strip() == flight.arr_at.strip():
                    flight.arr_dest = destination

        return flights
    
    def print_upcoming_flights(self):
        self.print_flights(self.get_all_upcoming_flights())

    def print_past_flights(self):
        self.print_flights(self.get_all_past_flights())

    def print_flights(self, flights):
        for flight in flights:
            print(flight)

    def register_flight(self, flight):
        """Registers flight in the upcoming_flights.csv"""
        return self.data_wrapper.register_flight(flight)

    def get_all_flights_from_one_airport(self, airport):
        return self.data_wrapper.get_all_flights_from_one_airport(airport)
    
    def get_employee_past_schedule_by_nid(self, kennitala):
        return self.data_wrapper.get_employee_past_schedule_by_nid(kennitala)
    

    def generate_flight_nr(self):
        """Generates a unique random flight number"""

        four_digit_random_number = random.randrange(1000, 10000)
        four_digit_random_number = "WRONGNA" + str(four_digit_random_number)
        all_flight_nr = self.data_wrapper.get_all_flight_nr()

        while four_digit_random_number in all_flight_nr:
            four_digit_random_number = random.randrange(1000, 10000)
            four_digit_random_number = "WRONGNA" + str(four_digit_random_number)

        return four_digit_random_number
    

    def get_avaiable_fligths_by_date(self, date):
        """Returns a list of flights available for an inputed date"""

        past_schedule = self.data_wrapper.get_all_past_flights()
        upcoming_schedule = self.data_wrapper.get_all_upcoming_flights()
        all_flights = past_schedule + upcoming_schedule
        flights_on_date = [] 

        for flight in all_flights:
            if date in self.logic_utils.generate_date_range(flight.depart_date, flight.arr_date):
                flights_on_date.append(flight)

        return flights_on_date
    
    def get_non_available_flights_by_date(self, date):
        """Returns a list of flights not available for an inputed date"""
        past_schedule = self.data_wrapper.get_all_past_flights()
        upcoming_schedule = self.data_wrapper.get_all_upcoming_flights()
        all_flights = past_schedule + upcoming_schedule
        flights_on_date = [] 

        for flight in all_flights:
            if date not in self.logic_utils.generate_date_range(flight.depart_date, flight.arr_date):
                flights_on_date.append(flight)

        return flights_on_date
