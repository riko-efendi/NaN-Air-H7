from model.flight import Flight


class Voyage:
    def __init__(self, flight_1:Flight, flight_2:Flight, pilots=[], cabin_crew=[]) -> None:
        self.id = flight_1.flight_nr + flight_2.flight_nr
        self.flight_1 = flight_1
        self.flight_2 = flight_2
        self.flight_1_dest = self.flight_1.dep_from


    def __str__(self) -> str:
        return f"Voyage ID: {self.id}, Going from {self.flight_1.dep_from} to {self.flight_1.arr_at}, then back to {self.flight_2.arr_at}"
