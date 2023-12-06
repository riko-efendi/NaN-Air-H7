import csv

from model.flight import Flight

class FlightData:
    def __init__(self) -> None:
        self.file_name = "_PROJECT/files/past_flights.csv"
        self.file_name2 = "_PROJECT/files/upcoming_flights.csv"

    def read_all_past_flights(self):
        past_flight_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                past_flight_list.append(Flight(row["flight_nr"], row["dep_from"], row["arr_at"], row["aircraft_id"]))
        return past_flight_list
        
    def read_all_upcoming_flights(self):
        upcoming_flight_list = []
        with open(self.file_name2, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                upcoming_flight_list.append(Flight(row["flight_nr"], row["dep_from"], row["arr_at"], row["departure"], row["arrival"]))
        return upcoming_flight_list