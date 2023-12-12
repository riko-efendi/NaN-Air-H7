
from data.employee_data import EmployeeData
from logic.aircraft_logic import AircraftLogic
from logic.flight_logic import FlightLogic
from logic.voyage_logic import VoyageLogic

from data.data_wrapper import DataWrapper

from model.employee import Employee
from model.aircraft import Aircraft

from utils.logic_utils import LogicUtils

class EmployeeLogic:
    def __init__(self, data_connection:DataWrapper) -> None:
        self.logic_utils = LogicUtils()
        self.data_wrapper = data_connection
        self.flight_logic = FlightLogic(self.data_wrapper)
        self.voyage_logic = VoyageLogic(self.data_wrapper)

    def get_all_employees(self) -> list[Employee]:  
        employees = []

        for employee in self.data_wrapper.get_all_employees():
            employee_working_days =  self.get_working_days_of_employee(employee)
            if employee_working_days != None:
                employee.work_days = employee_working_days
            else:
                employee.work_days = []

            employees.append(employee)

        return employees
    
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

        all_employees = self.get_all_employees()
        returned_employees = []
       
        for employee in all_employees:
            if employee.role == role or role == "":
                if employee.rank == rank or rank == "":
                    returned_employees.append(employee)

        return returned_employees
    

    def get_working_days_of_employee(self, employee):
        """Inject work schedule in employee"""
        
        all_upcoming_voyages = self.voyage_logic.get_all_upcoming_voyages()

        # working_employees = []

        # I get all the flights
        for voyage in all_upcoming_voyages:
            # Get all nids from flight
            for crew in voyage.all_crew:
                # Create employee from nid
                if crew == employee.kennitala:
                        # Put working days in work days, using the dates of the flight
                    return self.logic_utils.generate_date_range(voyage.depart_date, voyage.arr_date)
                        # working_employees.append(e)

        # return working_employees
    
    def get_available_employees(self, depart_date, arr_date, role, rank):
        employee_of_role = self.get_all_employees_by_role_rank(role, rank)
        
        working_dates = self.logic_utils.generate_date_range(depart_date, arr_date)
        available_employees = []

        for employee in employee_of_role:
            # If a date is not in work days is in working_dates
            common_days = [days for days in employee.work_days if days in working_dates]

            if common_days == []:
                available_employees.append(employee)

        return available_employees