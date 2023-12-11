
from data.employee_data import EmployeeData
from logic.aircraft_logic import AircraftLogic
from logic.flight_logic import FlightLogic

from data.data_wrapper import DataWrapper

from model.employee import Employee
from model.aircraft import Aircraft


class EmployeeLogic:
    def __init__(self, data_connection:DataWrapper) -> None:
        self.data_wrapper = data_connection

    def get_all_employees(self) -> list[Employee]:  
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

    def get_all_flightservicemanagers(self):
        return self.data_wrapper.get_all_flightservicemanagers()
    
    def get_all_flightattendants(self):
        return self.data_wrapper.get_all_flightattendants()
    
    def get_employees_past_schedule_by_date(self, date):
        return self.data_wrapper.get_employees_past_schedule_by_date(date)

    def get_all_pilots_by_license(self, license):
        return self.data_wrapper.get_all_pilots_by_license(license)
    

    def get_all_employees_by_role_rank(self, role:str="", rank:str=""):
        """Gets all employees by an inputed role and rank"""

        all_employees = self.data_wrapper.get_all_employees()
        returned_employees = []
       
        for employee in all_employees:
            if employee.role == role or role == "":
                if employee.rank == rank or rank == "":
                    returned_employees.append(employee)

        return returned_employees




