from logic.employee_logic import EmployeeLogic
from logic.aircraft_logic import AircraftLogic
from data.data_wrapper import DataWrapper

class LogicWrapper:
    def __init__(self) -> None:

        self.data_wrapper = DataWrapper()

        self.data_wrapper = DataWrapper()
        self.employee_logic = EmployeeLogic(self.data_wrapper)
        self.aircraft_logic = AircraftLogic(self.data_wrapper)
        
    def get_all_employees(self):
        return self.employee_logic.get_all_employees()
    
    def get_all_aircrafts(self):
        return self.aircraft_logic.get_all_aircrafts()
