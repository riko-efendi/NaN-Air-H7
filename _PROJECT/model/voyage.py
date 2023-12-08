from model.flight import Flight
from model.employee import Employee

"""
Voyage base class. Here we give the voyage all its variables, and behaviours.
"""

class Voyage:
    def __init__(self, fid:"Flight"=None, flight_out:"Flight"=None, flight_in:"Flight"=None, pilot:"Employee"=None, cabincrew:"Employee"=None) -> None:
        self.fid = fid
        self.flight_out = flight_out
        self.flight_in = flight_in
        self.pilot = pilot
        self.cabincrew = cabincrew