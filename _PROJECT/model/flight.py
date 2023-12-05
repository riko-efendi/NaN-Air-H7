from datetime import time
from destination import Destination

"""
Flight base class. Here we give the flight all its variables, and behaviours.
"""

class Flight:
    def __init__(self, depart_country:"Destination"=None, depart_time:time=0, arrival_country:"Destination"=None, arrival_time:time=0) -> None:
        self.depart_country = depart_country
        self.depart_time = depart_time
        self.arrival_country = arrival_country
        self.arrival_time = arrival_time