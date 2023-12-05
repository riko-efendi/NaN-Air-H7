from logic.employee_logic import EmployeeLogic
from data.data_wrapper import DataWrapper

"""
Employee base class. Here we give the employee all its variables, and behaviours.
"""

class LogicWrapper:
    def __init__(self) -> None:

        self.data_wrapper = DataWrapper()

        self.employee_logic = EmployeeLogic(self.data_wrapper)

    def get_all_employees(self):
        return self.employee_logic.get_all_employees()

