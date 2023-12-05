from datetime import time

class Destination:
    def __init__(self, name:str="", airport:str="", numeric_id:int=0) -> None:
        self.name = name
        self.airport = airport
        self.numeric_id = numeric_id
        # self.flight_time = flight_time
        # self.flight_distance = flight_distance
        # self.contact_name = contact_name
        # self.contact_num = contact_num
