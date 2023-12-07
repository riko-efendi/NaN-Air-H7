import csv

from model.employee import Employee

class EmployeeData:
    def __init__(self) -> None:
        self.file_name = "_PROJECT/files/crew.csv"
        self.aircraft_file = "_PROJECT/files/aircraft_type.csv"

    def read_all_employees(self):
        """Reads names and info from the "crew.csv" file, and returns a list containing that information."""

        employee_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                employee_list.append(Employee(row["nid"], row["name"], row["role"], row["rank"], row["address"], row["phone_nr"]))
        return employee_list
    

    def register_employee(self, employee) -> None:
        """Writes employee info oto the crew.csv file"""

        fieldnames = ["nid", "name", "role", "rank", "licence", "address","phone_nr","slot_param"]
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"nid": employee.kennitala, "name": employee.name, "role": employee.role, "rank":employee.rank, "address": employee.address, "phone_nr": employee.phone_number})

    def read_all_pilots(self):
        pilot_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["role"] == "Pilot":
                    pilot_list.append(Employee(row["nid"], row["name"], row["role"]))
        return pilot_list
    
    def read_all_cabincrews(self):
        cabincrew_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["role"] == "Cabincrew":
                    cabincrew_list.append(Employee(row["nid"], row["name"], row["role"]))
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
        fieldnames = ["nid", "name", "role", "rank", "licence", "address","phone_nr","slot_param"]

        with open(self.file_name, 'w', newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

        for employee in employees:
            if employee.kennitala == kennitala:
                employee.address = address
                employee.phone_number = phone_number
            self.register_employee(employee)
