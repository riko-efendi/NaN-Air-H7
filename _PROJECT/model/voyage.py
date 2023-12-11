from model.flight import Flight
from model.employee import Employee

"""
Voyage base class. Here we give the voyage all its variables, and behaviours.
"""

class Voyage:
    def __init__(self, fid:"Flight"=None, flights:"Flight"=None, pilot:"Employee"=None, cabincrew:"Employee"=None) -> None:
        self.fid = fid
        self.flights = flights
        self.pilot = pilot
        self.cabincrew = cabincrew
