from data.aircraft_data import AircraftData

class AircraftLogic:
    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection

    def get_all_aircrafts(self):
        return self.data_wrapper.get_all_aircrafts()