from data.aircraft_data import AircraftData
<<<<<<< HEAD
from model.aircraft import Aircraft

=======
>>>>>>> 50f6add73441a8db699aaa422da6b0dfba2cce87

class AircraftLogic:
    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection

    def get_all_aircrafts(self):
        return self.data_wrapper.get_all_aircrafts()