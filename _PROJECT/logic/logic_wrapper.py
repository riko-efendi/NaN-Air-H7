from logic.employee_logic import EmployeeLogic
from logic.destination_logic import DestinationLogic
from logic.flight_logic import FlightLogic
from logic.aircraft_logic import AircraftLogic
from data.data_wrapper import DataWrapper

"""
Employee base class. Here we give the employee all its variables, and behaviours.
"""

class LogicWrapper:
    def __init__(self) -> None:
        self.data_wrapper = DataWrapper()
        self.employee_logic = EmployeeLogic(self.data_wrapper)
        self.destination_logic = DestinationLogic(self.data_wrapper)
        self.flight_logic = FlightLogic(self.data_wrapper)
        self.aircraft_logic = AircraftLogic(self.data_wrapper)

    # EMPLOYEE

    def get_all_employees(self):
        return self.employee_logic.get_all_employees()

    def get_employee_by_nid(self, kennitala):
        return self.employee_logic.get_employee_by_nid(kennitala)
    
    def register_employee(self, employee):
        return self.employee_logic.register_employee(employee)

    def get_all_pilots(self):
        return self.employee_logic.get_all_pilots()
    
    def get_all_cabincrews(self):
        return self.employee_logic.get_all_cabincrews()
    
    def get_all_flightservicemanagers(self):
        return self.employee_logic.get_all_flightservicemanagers()
    
    def get_all_flightattendants(self):
        return self.employee_logic.get_all_flightattendants()
    
    def update_employee_info(self, kennitala, address, phone_number):
        return self.employee_logic.update_employee_info(kennitala, address, phone_number)
    
    def get_all_captain_pilots(self):
        return self.employee_logic.get_all_captain_pilots()
    
    def get_all_pilots_by_license(self, license):
        return self.employee_logic.get_all_pilots_by_license(license)
    
    def get_all_copilots(self):
        return self.employee_logic.get_all_copilots()
    # DESTINATIONS

    def get_all_destinations(self):
        return self.destination_logic.get_all_destinations()
    
    def create_destination(self, destination):
        return self.destination_logic.create_destination(destination)

    
    # FLIGHTS

    def get_all_upcoming_flights(self):
        return self.flight_logic.get_all_upcoming_flights()
    
    def get_all_past_flights(self):
        return self.flight_logic.get_all_past_flights()
    
    def print_all_upcoming_flights(self):
        return self.flight_logic.print_upcoming_flights()
    
    def print_all_past_flights(self):
        return self.flight_logic.print_past_flights()

    def get_all_aircrafts(self):
        return self.aircraft_logic.get_all_aircrafts()
    
    
    
    
