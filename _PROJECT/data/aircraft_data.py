import csv
from model.aircraft import Aircraft

class AircraftData:
    def __init__(self) -> None:
        self.file_name = "aircraft.csv"

    def read_all_aircrafts(self):
        """Read aircraft.csv and return list of all aircrafts information"""
        aircraft_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                aircraft_list.append(Aircraft(row["plane_insignia"], row["plane_type_id"], row["date_of_manufacture"], row["last_maintenance"]))
        return aircraft_list
