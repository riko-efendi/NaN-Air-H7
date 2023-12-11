from data.aircraft_data import AircraftData

class AircraftLogic:
    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection

    def get_all_aircrafts(self):
        """Returns a list of all aircrafts"""
        return self.data_wrapper.get_all_aircrafts()
    
    def get_all_aircraft_type(self):
        """Returns a list containing the type of aircraft"""

        ids = set()
        aircrafts = self.data_wrapper.get_all_aircrafts()
        for aircraft in aircrafts:
            ids.add(aircraft.plane_type_id)

        return list(ids)
