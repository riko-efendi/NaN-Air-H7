from flight import Flight

class Voyage:
    def __init__(self, name:str="", airport:str="", flight_out:"Flight"=None, flight_in:"Flight"=None) -> None:
        self.name = name
        self.airport = airport
        self.flight_out = flight_out
        self.flight_in = flight_in