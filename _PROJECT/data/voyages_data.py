import csv

class VoyagesData:
    def __init__(self) -> None:
        self.file_name = "_Projekkdfdlksfj"
        self.fieldnames = ["nid", "name", "role", "rank", "licence", "address", "phone_nr", "slot_param"]
        
    def register_employee(self, employee):

        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:

            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)

            writer.writerow({"nid": employee.kennitala, "name": employee.name, "role": employee.role, "rank":employee.rank, "address": employee.address, "phone_nr": employee.phone_number})