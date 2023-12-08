from model.voyage import Voyage
from logic.employee_logic import EmployeeLogic
from logic.flight_logic import FlightLogic

class VoyagesLogic:
    def __init__(self, voyage) -> None:
        self.file_name = "voyages.csv"
        self.flight_logic = FlightLogic(voyage)
        self.employee_logic = EmployeeLogic(voyage)

    def create_voyage(self):
        flight_list = self.flight_logic.get_all_upcoming_flights()
        print(flight_list)
        return print(flight_list)

    def search_flights(self):     
        flight_list = self.flight_logic.get_all_upcoming_flights()
        print(flight_list)

        return 
        
    
    def search_employees(self):
        cabin_crew_list = self.employee_logic.get_all_cabincrews()
        pilot_list = self.employee_logic.get_all_pilots()
        print(pilot_list)

        return