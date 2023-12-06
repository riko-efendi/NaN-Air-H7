from datetime import time



"""
Flight base class. Here we give the flight all its variables, and behaviours.
"""

class Flight:
    def __init__(self, flight_nr, dep_from, arr_at, departure, arrival, aircraft_id=None) -> None:

        depart_date, depart_time = departure.split(" ")
        arr_date, arr_time = arrival.split(" ")
        self.flight_nr = flight_nr
        self.aircraft_id = aircraft_id

        # DEPARTURE
        self.dep_from = dep_from
        self.depart_date = depart_date
        self.depart_time = depart_time
        self.depart_dest = None

        # ARRIVAL
        self.arr_at = arr_at
        self.arr_date = arr_date
        self.arr_time = arr_time
        self.arr_dest = None

    def __str__(self) -> str:
        return_str = f"Flight number: {self.flight_nr}. Departing from {self.dep_from} and arriving at {self.arr_at}."

        return return_str