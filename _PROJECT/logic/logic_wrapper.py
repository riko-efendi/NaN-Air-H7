from logic.employee_logic import EmployeeLogic
from logic.destination_logic import DestinationLogic

from data.data_wrapper import DataWrapper

class LogicWrapper:
    def __init__(self) -> None:

        self.data_wrapper = DataWrapper()
        self.employee_logic = EmployeeLogic(self.data_wrapper)
        self.destination_logic = DestinationLogic(self.data_wrapper)

    def get_all_employees(self):
        return self.employee_logic.get_all_employees()

    def get_all_destinations(self):
        return self.destination_logic.get_all_destinations()

