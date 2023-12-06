from logic.employee_logic import EmployeeLogic
from logic.destination_logic import DestinationLogic
from data.data_wrapper import DataWrapper

"""
Employee base class. Here we give the employee all its variables, and behaviours.
"""

class LogicWrapper:
    def __init__(self) -> None:
        self.data_wrapper = DataWrapper()
        self.employee_logic = EmployeeLogic(self.data_wrapper)
        self.destination_logic = DestinationLogic(self.data_wrapper)

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

    def get_all_destinations(self):
        return self.destination_logic.get_all_destinations()
    
    def create_destination(self, destination):
        return self.destination_logic.create_destination(destination)

    def get_all_upcoming_flights(self):
        return self.flight_logic.get_all_upcoming_flights()

    def get_all_past_flights(self):
        return self.flight_logic.get_all_past_flights()

    def print_all_upcoming_flights(self):
        return self.flight_logic.print_upcoming_flights()

    def print_all_past_flights(self):
        return self.flight_logic.print_past_flights()