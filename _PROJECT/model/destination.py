from datetime import time

"""
Destination base class. Here we give the destination all its variables, and behaviours.
"""

class Destination:
    def __init__(self, id:str="", destination:str="", numeric_id:int=0) -> None:

        self.id = id
        self.destination = destination
        self.numeric_id = numeric_id
        # self.flight_time = flight_time
        # self.flight_distance = flight_distance
        # self.contact_name = contact_name
        # self.contact_num = contact_num
