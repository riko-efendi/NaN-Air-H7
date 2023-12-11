from datetime import datetime



"""
Flight base class. Here we give the flight all its variables, and behaviours.
"""

class Flight:
    def __init__(self, flight_nr:str="", dep_from:str="", arr_at:str="", departure:str=". .", arrival:str=". .", aircraft_id=None) -> None:


        depart_date, depart_time = departure.split(" ")
        arr_date, arr_time = arrival.split(" ")
        self.flight_nr = flight_nr
        self.aircraft_id = aircraft_id
        self.duration = 0

        # DEPARTURE
        self.dep = departure
        self.dep_from = dep_from
        self.depart_date = depart_date
        self.depart_time = depart_time
        self.depart_dest = None

        # ARRIVAL
        self.arr = arrival
        self.arr_at = arr_at
        self.arr_date = arr_date
        self.arr_time = arr_time
        self.arr_dest = None



    
    def __str__(self) -> str:
        return_str = f"Flight number: {self.flight_nr}.\nDeparting from:\t{self.dep_from} \t[{self.depart_date} {self.depart_time}]\nArriving at:\t{self.arr_at} \t[{self.arr_date} {self.arr_time}]"
        return_str += f"\nThe duration of the flight is {self.flight_dur}\n"
        return return_str
    
    
    def calculate_flight_duration(self, time_1, time_2):
        time_format = "%H:%M:%S"
        time_1 = datetime.strptime(time_1, time_format)
        time_2 = datetime.strptime(time_2, time_format)

        return time_2 - time_1