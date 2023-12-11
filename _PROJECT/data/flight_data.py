import csv

from model.flight import Flight

class FlightData:
    def __init__(self) -> None:
        self.file_name_past = "_PROJECT/files/past_flights.csv"
        self.file_name_upcoming = "_PROJECT/files/upcoming_flights.csv"
        self.fieldnames = ["flight_nr", 
                           "dep_from", 
                           "arr_at", 
                           "departure_date", 
                           "departure_time", 
                           "arrival_date", 
                           "arrival_time",
                           "captain",
                           "copilot",
                           "fsm",
                           "fa1",
                           "fa2"]

    def read_all_past_flights(self):
        past_flight_list = []
        with open(self.file_name_past, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                past_flight_list.append(Flight(row["flight_nr"], 
                                               row["dep_from"], 
                                               row["arr_at"], 
                                               row["departure_date"], 
                                               row["departure_time"], 
                                               row["arrival_date"], 
                                               row["arrival_time"], 
                                               row["aircraft_id"]))
        return past_flight_list
        
    def read_all_upcoming_flights(self):
        upcoming_flight_list = []
        with open(self.file_name_upcoming, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                upcoming_flight_list.append(Flight(row["flight_nr"], 
                                                   row["dep_from"], 
                                                   row["arr_at"], 
                                                   row["departure_date"], 
                                                   row["departure_time"], 
                                                   row["arrival_date"], 
                                                   row["arrival_time"]))
        
        return upcoming_flight_list
    
    def read_all_flights_from_one_airport(self, airport):
        all_flights_from_one_airport_list = []
        with open(self.file_name_upcoming, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["dep_from"] == airport:
                    all_flights_from_one_airport_list.append(Flight(row["flight_nr"], 
                                                                    row["dep_from"], 
                                                                    row["arr_at"], 
                                                                    row["departure_date"], 
                                                                    row["departure_time"], 
                                                                    row["arrival_date"], 
                                                                    row["arrival_time"]))
        return all_flights_from_one_airport_list
    
    def read_employee_past_schedule_by_nid(self, kennitala):
        schedule_list = []
        with open(self.file_name_past, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["captain"] == kennitala or row["copilot"] == kennitala or row["fsm"] == kennitala or row["fa1"] == kennitala or row["fa2"] == kennitala:
                    schedule_list.append(Flight(row["flight_nr"], row["dep_from"], row["arr_at"], row["departure"], row["arrival"], row["captain"], row["copilot"], row["fsm"], row["fa1"], row["fa2"], row["aircraft_id"]))

        return schedule_list
    

    
    def register_flight(self, flight:Flight) -> None:
        """Writes employee info onto the crew.csv file"""

        with open(self.file_name_upcoming, 'a', newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writerow({"flight_nr": flight.flight_nr, 
                             "dep_from": flight.dep_from, 
                             "arr_at": flight.arr_at, 
                             "departure_date": flight.depart_date, 
                             "departure_time": flight.depart_time, 
                             "arrival_date": flight.arr_date, 
                             "arrival_time": flight.arr_time,
                             "captain": flight.captain, 
                             "copilot": flight.copilot,
                             "fsm": flight.fsm,
                             "fa1": flight.fa1})


    def read_all_flight_nr(self):
        """Returns a list of all flight numbers"""
        flight_nrs = []

        with open(self.file_name_upcoming, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                flight_nrs.append(row["flight_nr"])
        return flight_nrs

