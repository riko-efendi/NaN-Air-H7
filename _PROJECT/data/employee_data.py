import csv

from model.employee import Employee

class EmployeeData:
    def __init__(self) -> None:
        self.file_name = "_PROJECT/files/crew.csv"

    def read_all_employees(self):
        """Reads names and info from the "crew.csv" file, and returns a list containing that information."""

        employee_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                employee_list.append(Employee(row["nid"], row["name"], row["role"]))
        return employee_list
    

    def register_employee(self, employee):

        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["nid", 
                          "name", 
                          "role", 
                          "rank", 
                          "licence", 
                          "address",
                          "phone_nr",
                          "slot_param"]
            
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

    def update_employee_info(self, nid):
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                return row['address'], row['phone_nr']
            
        with open(self.file_name, 'w', newline="", encoding="utf-8") as csvfile:
            fieldnames = [
                "role",
                "rank",
                "license",
                "address",
                "phone_nr",
            ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        with open(self.file_name, 'w', newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(nid)
