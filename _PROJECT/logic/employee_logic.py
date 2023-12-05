from data.employee_data import EmployeeData
from model.employee import Employee

class EmployeeLogic:
    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection

    def get_all_employees(self):
        return self.data_wrapper.read_all_employees()