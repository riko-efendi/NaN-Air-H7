from data.employee_data import EmployeeData
from data.flight_data import FlightData
from data.destination_data import DestinationData
from data.aircraft_data import AircraftData
from data.voyages_data import VoyageData

class DataWrapper:
    def __init__(self) -> None:
        self.employee_data = EmployeeData()
        self.flight_data = FlightData()
        self.destination_data = DestinationData()
        self.aircraft_data = AircraftData()
        self.voyage_data = VoyageData
    #Employees
    def get_all_employees(self):
        return self.employee_data.read_all_employees()

    def register_employee(self, employee):
        return self.employee_data.register_employee(employee)
    
    def update_employee_info(self, kennitala, address, phone_number):
        return self.employee_data.update_employee_info(kennitala, address, phone_number)

    def get_all_pilots(self):
        return self.employee_data.read_all_pilots()
    
    def get_all_pilots_by_license(self, license):
        return self.employee_data.read_all_pilots_by_license(license)
    
    def get_all_captain_pilots(self):
        return self.employee_data.read_all_captain_pilots()
    
    def get_all_copilots(self):
        return self.employee_data.read_all_copilots()
    
    def get_all_cabincrews(self):
        return self.employee_data.read_all_cabincrews()
    
    def get_all_flightservicemanagers(self):
        return self.employee_data.reaf_all_flightservicemanagers()
    
    def get_all_flightattendants(self):
        return self.employee_data.read_all_flightattendants()
    
    # SCHEDULE
    
    def get_employee_past_schedule_by_nid(self, kennitala):
        return self.flight_data.read_employee_past_schedule_by_nid(kennitala)
    
    def get_employees_past_schedule_by_date(self, date):
        return self.employee_data.read_employees_past_schedule_by_date(date)
    
    def get_employees_past_schedule_by_date_range_and_kennitala(self, start_date, end_date, kennitala):
        return self.employee_data.read_employees_past_schedule_by_date_range_and_kennitala(start_date, end_date, kennitala)
    
    # FLIGHTS

    def get_all_past_flights(self):
        return self.flight_data.read_all_past_flights()
    
    def get_all_upcoming_flights(self):
        return self.flight_data.read_all_upcoming_flights()
    
    def get_all_flights_from_one_airport(self, airport):
        return self.flight_data.read_all_flights_from_one_airport(airport)
    
    def get_all_flight_nr(self):
        return self.flight_data.read_all_flight_nr()
    
    def register_flight(self, flight):
        return self.flight_data.register_flight(flight)
    
    
    # DESTINATIONS
    
    def get_all_destinations(self):
        return self.destination_data.read_all_destinations()
    
    def register_destination(self, destination):
        return self.destination_data.register_destination(destination)
    
    # AIRCRAFTS

    def get_all_aircrafts(self):
        return self.aircraft_data.read_all_aircrafts()
    
    #Voyages
    def get_all_voyages(self):
        return self.voyage_data.get_all_voyages()

    def create_new_voyage(self):
        return self.voyage_data.create_new_voyage()
    
    
