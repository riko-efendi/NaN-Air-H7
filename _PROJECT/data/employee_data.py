import csv

from model.employee import Employee

class EmployeeData:
    def __init__(self) -> None:
        self.file_name = "_PROJECT/files/crew.csv"

    def read_all_employees(self):
        employee_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                employee_list.append(Employee(row["nid"], row["name"], row["role"]))
        return employee_list
    
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