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

    def register_employee(self, employee):
        return self.employee_data.register_employee(employee)
    
    def update_employee_info(self, kennitala, address, phone_number):
        return self.employee_data.update_employee_info(kennitala, address, phone_number)

    def get_all_pilots(self):
        return self.employee_data.read_all_pilots()
    
    def get_all_cabincrews(self):
        return self.employee_data.read_all_cabincrews()
    
    # FLIGHTS

    def get_all_past_flights(self):
        return self.flight_data.read_all_past_flights()
    
    def get_all_upcoming_flights(self):
        return self.flight_data.read_all_upcoming_flights()
    
    # DESTINATIONS
    
    def get_all_destinations(self):
        return self.destination_data.read_all_destinations()
    
    def create_destination(self, destination):
        return self.destination_data.create_destination(destination)
    
    # AIRCRAFTS

    def get_all_aircrafts(self):
        return self.aircraft_data.read_all_aircrafts()

    def get_all_pilots_by_license(self, license):
        return self.employee_data.read_all_pilots_by_license(license)
