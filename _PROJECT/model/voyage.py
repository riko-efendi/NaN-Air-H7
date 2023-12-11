from model.flight import Flight
<<<<<<< HEAD
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
=======

class Voyage:
    def __init__(self, flight_1:Flight, flight_2:Flight) -> None:
        self.id = flight_1.flight_nr + flight_2.flight_nr
        self.flight_1 = flight_1
        self.flight_2 = flight_2

    def __str__(self) -> str:
        return f"Voyage id: {self.id}\nGoing from KEF to {self.flight_1.arr_at}"
>>>>>>> eead74ee80ec091cc353a879a80a68552811e54a
