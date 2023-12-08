import csv
<<<<<<< HEAD
=======

>>>>>>> 50f6add73441a8db699aaa422da6b0dfba2cce87
from model.aircraft import Aircraft

class AircraftData:
    def __init__(self) -> None:
<<<<<<< HEAD
        self.file_name = "_PROJECT/filesaircraft.csv"

    def read_all_aicrafts(self):
        aicraft_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                aicraft_list.append(Aircraft(row["plane_insignia"],row["plane_type_id"],row["date_of_manufacture"],row["last_maintenance"]))
        return aicraft_list
=======
        self.file_name = "_PROJECT/files/aircraft.csv"

    def read_all_aircrafts(self):
        aircraft_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                aircraft_list.append(Aircraft(row["plane_insignia"], row["plane_type_id"], row["date_of_manufacture"], row["last_maintenance"]))
        return aircraft_list
>>>>>>> 50f6add73441a8db699aaa422da6b0dfba2cce87
