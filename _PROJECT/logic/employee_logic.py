
from data.employee_data import EmployeeData
from logic.aircraft_logic import AircraftLogic

from model.employee import Employee
from model.aircraft import Aircraft

class EmployeeLogic:
    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection

    def get_all_employees(self):
        return self.data_wrapper.get_all_employees()
    
    def get_employee_by_nid(self, kennitala):
        for employee in self.data_wrapper.get_all_employees():
            if kennitala == employee.kennitala:
                return employee
            
    def update_employee_info(self, kennitala, address, phone_number):
        return self.data_wrapper.update_employee_info(kennitala, address, phone_number)

    def register_employee(self, employee):
        return self.data_wrapper.register_employee(employee)

    def get_all_pilots(self):
        return self.data_wrapper.get_all_pilots()
    
    def get_all_cabincrews(self):
        return self.data_wrapper.get_all_cabincrews()

    def get_all_pilots_by_license(self, license):
        return self.data_wrapper.get_all_pilots_by_license(license)

                    
