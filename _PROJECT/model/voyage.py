from model.flight import Flight
from model.employee import Employee

"""
Voyage base class. Here we give the voyage all its variables, and behaviours.
"""

class Voyage:
    def __init__(self, flight_1:Flight, flight_2:Flight) -> None:
        self.id = flight_1.flight_nr + flight_2.flight_nr
        self.flight_1 = flight_1
        self.flight_2 = flight_2

        self.depart_date = flight_1.depart_date
        self.arr_date = flight_2.arr_date

        self.crew = flight_1.crew

    def __str__(self) -> str:
        return f"Voyage id: {self.id}\n\tGoing from KEF to {self.flight_1.arr_at}"
