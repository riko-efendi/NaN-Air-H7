from data.employee_data import EmployeeData
from data.flight_data import FlightData
from data.destination_data import DestinationData

class DataWrapper:
    def __init__(self) -> None:
        self.employee_data = EmployeeData()
        self.flight_data = FlightData()
        self.destination_data = DestinationData()

    def get_all_employees(self):
        return self.employee_data.read_all_employees()

    def register_employee(self, employee):
        return self.employee_data.register_employee(employee)

    def get_all_pilots(self):
        return self.employee_data.read_all_pilots()
    
    def get_all_cabincrews(self):
        return self.employee_data.read_all_cabincrews()
    
    def get_all_past_flights(self):
        return self.flight_data.read_all_past_flights()
    
    def get_all_upcoming_flights(self):
        return self.flight_data.read_all_upcoming_flights()
    
    def get_all_destinations(self):
        return self.destination_data.read_all_destinations()
    
    def create_destination(self, destination):
        return self.destination_data.create_destination(destination)