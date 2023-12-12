import csv
from datetime import datetime

from model.employee import Employee
from model.flight import Flight

class EmployeeData:
    def __init__(self) -> None:
        self.file_name = "_PROJECT/files/crew.csv"
        self.aircraft_file = "_PROJECT/files/aircraft_type.csv"
        self.past_flight_file= "_PROJECT/files/past_flights.csv"
        self.fieldnames = ["nid", "name", "role", "rank", "licence", "address","phone_nr","slot_param"]


    def read_all_employees(self):
        """Reads names and info from the "crew.csv" file, and returns a list containing that information."""

        employee_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                employee_list.append(Employee(row["nid"], row["name"], row["role"], row["rank"], row["address"], row["phone_nr"]))
        return employee_list
        
    
    def register_employee(self, employee:Employee) -> None:
        """Writes employee info onto the crew.csv file"""

        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writerow({"nid": employee.kennitala, "name": employee.name, "role": employee.role, "rank":employee.rank, "address": employee.address, "phone_nr": employee.phone_number})


    def read_all_pilots(self):
        pilot_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["role"] == "Pilot":
                    pilot_list.append(Employee(row["nid"], row["name"], row["role"], row["rank"], row["address"], row["phone_nr"]))
        return pilot_list
    

    def read_all_cabincrews(self):
        cabincrew_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["role"] == "Cabincrew":
                    cabincrew_list.append(Employee(row["nid"], row["name"], row["role"], row["rank"], row["address"], row["phone_nr"]))
        return cabincrew_list
    
    def read_all_pilots_by_license(self, license):
        pilot_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["license"] == license:
                    pilot_list.append(row["name"])
        return pilot_list


    def update_employee_info(self, kennitala, address, phone_number):
        """Updates the info of a specific employee, then re-writes the whole document"""
        employees = self.read_all_employees()

        with open(self.file_name, 'w', newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writeheader()

        for employee in employees:
            if employee.kennitala == kennitala:
                employee.address = address
                employee.phone_number = phone_number
            self.register_employee(employee)

    def read_employees_past_schedule_by_date(self, date):
        past_schedule_list = []
        employees = self.read_all_employees()
        with open(self.past_flight_file, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                depart_date = row["departure_date"]
                if depart_date == date:
                    past_schedule_list.append(Flight(row["flight_nr"], row["dep_from"], row["arr_at"], row["departure_date"], row["departure_time"], row["arrival_date"], row["arrival_time"], row["captain"], row["copilot"], row["fsm"], row["fa1"], row["fa2"], row["aircraft_id"]))
        return past_schedule_list
    
    def read_employees_past_schedule_by_date_range_and_kennitala(self, start_date, end_date, kennitala):
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        flights_in_range = []

        with open(self.past_flight_file, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                departure_date = datetime.strptime(row['departure_date'], "%Y-%m-%d")
                if start_date <= departure_date <= end_date:
                    if kennitala and (kennitala in [row['captain'], row['copilot'], row['fsm'], row['fa1'], row['fa2']]):
                        flights_in_range.append(row)
        return flights_in_range