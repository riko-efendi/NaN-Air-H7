from datetime import time

class Destination:
    def __init__(self, name:str="", airport:str="", flight_time:time=0, flight_distance:float=0, contact_name:str="", contact_num:int=1111111) -> None:
        self.name = name
        self.airport = airport
        self.flight_time = flight_time
        self.flight_distance = flight_distance
        self.contact_name = contact_name
        self.contact_num = contact_num
