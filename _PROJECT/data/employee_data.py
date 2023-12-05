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

            writer.writerow({'name': employee.name, 'nid': employee.kennitala})