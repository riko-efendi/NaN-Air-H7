from data.employee_data import EmployeeData
from data.flight_data import FlightData
from data.destination_data import DestinationData
from data.aircraft_data import AircraftData

class DataWrapper:
    def __init__(self) -> None:
        self.employee_data = EmployeeData()
        self.flight_data = FlightData()
        self.destination_data = DestinationData()
        self.aircraft_data = AircraftData()

    def get_all_employees(self):
        return self.employee_data.read_all_employees()
    
    def get_all_past_flights(self):
        return self.flight_data.read_all_past_flights()
    
    def get_all_upcoming_flights(self):
        return self.flight_data.read_all_upcoming_flights()
    
    def get_all_destinations(self):
        return self.destination_data.read_all_destinations()
    
    def get_all_aircrafts(self):
        return self.aircraft_data.read_all_aicrafts()