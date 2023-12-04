from data.employee_data import EmployeeData

class DataWrapper:
    def __init__(self) -> None:
        self.employee_data = EmployeeData()

    def get_all_employees(self):
        return self.employee_data.read_all_employees()
    
    