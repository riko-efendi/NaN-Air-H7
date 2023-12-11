from datetime import time

"""
Destination base class. Here we give the destination all its variables, and behaviours.
"""

class Destination:
    def __init__(self, id:str="", destination:str="", numeric_id:str="", flight_time_from_kef:str="") -> None:

        self.id = id
        self.destination = destination
        self.numeric_id = numeric_id
        self.flight_time_from_kef = flight_time_from_kef

