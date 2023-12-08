from model.flight import Flight

"""
Voyage base class. Here we give the voyage all its variables, and behaviours.
"""

class Voyage:
    def __init__(self, fid, flight_out:"Flight"=None, flight_in:"Flight"=None) -> None:
        
        self.flight_out = flight_out
        self.flight_in = flight_in