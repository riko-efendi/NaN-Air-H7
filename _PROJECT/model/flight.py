from datetime import time
from destination import Destination

class Flight:
    def __init__(self, depart_country:"Destination" = "", depart_time:time=0, arrival_country:"Destination"="", arrival_time:time=0) -> None:
        self.depart_country = depart_country
        self.depart_time = depart_time
        self.arrival_country = arrival_country
        self.arrival_time = arrival_time