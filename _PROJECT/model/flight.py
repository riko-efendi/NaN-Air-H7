from datetime import datetime


"""
Flight base class. Here we give the flight all its variables, and behaviours.
"""

class Flight:
    def __init__(self, flight_nr="", dep_from="", arr_at="", departure_date="", departure_time="", arrival_date="", arrival_time="", crew={}, aircraft_id=None) -> None:

       
        self.flight_nr = flight_nr
        self.aircraft_id = aircraft_id
        self.duration = 0

        # DEPARTURE
        
        self.dep_from = dep_from
        self.depart_date = departure_date
        self.depart_time = departure_time
        self.depart_dest = None

        # ARRIVAL
        
        self.arr_at = arr_at
        self.arr_date = arrival_date
        self.arr_time = arrival_time
        self.arr_dest = None

        self.crew = crew
    
    def __str__(self) -> str:
        return_str = f"Flight number: {self.flight_nr}.\nDeparting from:\t{self.dep_from} \t[{self.depart_date} {self.depart_time}]\nArriving at:\t{self.arr_at} \t[{self.arr_date} {self.arr_time}]"
        return return_str
    
    
    def calculate_flight_duration(self, time_1, time_2):
        time_format = "%H:%M:%S"
        time_1 = datetime.strptime(time_1, time_format)
        time_2 = datetime.strptime(time_2, time_format)

        return time_2 - time_1
    
