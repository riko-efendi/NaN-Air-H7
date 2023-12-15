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
        """Read past_flights.csv file and return all past flights"""
        past_flight_list = []
        fa_rows = self.get_fa_amount("_PROJECT/files/past_flights.csv")
        with open(self.file_name_past, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                crew_dict = {"captain": row["captain"], "copilot": row["copilot"], "fsm": row["fsm"]}
                for fa_row in fa_rows:
                    crew_dict[fa_row] = row[fa_row]
                past_flight_list.append(Flight(row["flight_nr"], 
                                               row["dep_from"], 
                                               row["arr_at"], 
                                               row["departure_date"], 
                                               row["departure_time"], 
                                               row["arrival_date"], 
                                               row["arrival_time"],
                                               crew_dict))
        return past_flight_list
        
    def read_all_upcoming_flights(self):
        """Read upcoming_flights.csv file and return all upcoming flights"""
        upcoming_flight_list = []
        fa_rows = self.get_fa_amount("_PROJECT/files/upcoming_flights.csv")
        with open(self.file_name_upcoming, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                crew_dict = {"captain": row["captain"], 
                             "copilot": row["copilot"], 
                             "fsm": row["fsm"]}
                
                for fa_row in fa_rows:
                    crew_dict[fa_row] = row[fa_row]
                upcoming_flight_list.append(Flight(row["flight_nr"], 
                                                   row["dep_from"], 
                                                   row["arr_at"], 
                                                   row["departure_date"], 
                                                   row["departure_time"], 
                                                   row["arrival_date"], 
                                                   row["arrival_time"],
                                                   crew_dict))
               
        return upcoming_flight_list
    
    def read_all_flights_from_one_airport(self, airport):
        """Read upcoming_flights.csv and return list of flights from chosen airport."""

        all_flights_from_one_airport_list = []
        fa_rows = self.get_fa_amount("_PROJECT/files/upcoming_flights.csv")
        with open(self.file_name_upcoming, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                crew_dict = {"captain": row["captain"], "copilot": row["copilot"], "fsm": ["fsm"]}
                for fa_row in fa_rows:
                    crew_dict[fa_row] = row[fa_row]
                if row["dep_from"] == airport:
                    all_flights_from_one_airport_list.append(Flight(row["flight_nr"], 
                                                                    row["dep_from"], 
                                                                    row["arr_at"], 
                                                                    row["departure_date"], 
                                                                    row["departure_time"], 
                                                                    row["arrival_date"], 
                                                                    row["arrival_time"],
                                                                    crew_dict))
        return all_flights_from_one_airport_list
    
    def read_employee_past_schedule_by_nid(self, kennitala):
        """Read past_flights.csv and retrieve the past flight schedule for an employee based on Kennitala"""
        schedule_list = []
        fa_rows = self.get_fa_amount("_PROJECT/files/past_flights.csv")
        with open(self.file_name_past, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                crew_dict = {"captain": row["captain"], "copilot": row["copilot"], "fsm": ["fsm"]}
                for fa_row in fa_rows:
                    crew_dict[fa_row] = row[fa_row]
                if row["captain"] == kennitala or row["copilot"] == kennitala or row["fsm"] == kennitala or row["fa1"] == kennitala or row["fa2"] == kennitala:
                    schedule_list.append(Flight(row["flight_nr"], 
                                                row["dep_from"], 
                                                row["arr_at"], 
                                                row["departure_date"], 
                                                row["departure_time"], 
                                                row["arrival_date"], 
                                                row["arrival_time"], 
                                                fa_rows, 
                                                row["aircraft_id"]))
        return schedule_list
    

    
    def register_flight(self, flight:Flight) -> None:
        """Writes employee info onto the crew.csv file"""

        fieldnames = ["flight_nr", 
                      "dep_from", 
                      "arr_at", 
                      "departure_date", 
                      "departure_time", 
                      "arrival_date", 
                      "arrival_time",
                      "captain",
                      "copilot",
                      "fsm"]
        
        writewrow_dict = {"flight_nr": flight.flight_nr, 
                            "dep_from": flight.dep_from, 
                            "arr_at": flight.arr_at, 
                            "departure_date": flight.depart_date, 
                            "departure_time": flight.depart_time, 
                            "arrival_date": flight.arr_date, 
                            "arrival_time": flight.arr_time,
                            "captain": flight.crew["captain"],
                            "copilot": flight.crew["copilot"],
                            "fsm": flight.crew["fsm"]}
        
        # Get how many fa's there are before the new flight get registered
        fa_rows = self.get_fa_amount("_PROJECT/files/upcoming_flights.csv")

        # Get how many fa's there are in the flight to be registerd
        flight_fa_rows = [key for key in flight.crew if key.startswith("fa")]
        # If there are the new fa_rows will be the fa's from the flight
        if len(flight_fa_rows) > len(fa_rows):
            fa_rows = flight_fa_rows
            for fa_row in flight_fa_rows:
                fieldnames.append(fa_row)
        else:
            for row in fa_rows:
                fieldnames.append(row)

        
        for fa_row in flight_fa_rows:
            writewrow_dict[fa_row] = flight.crew[fa_row]

        # Now we will have to re-register all the flights again
        flights = self.read_all_upcoming_flights()

        with open(self.file_name_upcoming, 'w', newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

        for old_flight in flights:
            row_dict = {"flight_nr":old_flight.flight_nr, 
                        "dep_from":old_flight.dep_from, 
                        "arr_at":old_flight.arr_at, 
                        "departure_date":old_flight.depart_date, 
                        "departure_time":old_flight.depart_time,
                        "arrival_date":old_flight.arr_date,
                        "arrival_time":old_flight.arr_time,}
            
            for crew in old_flight.crew:
                row_dict[crew] = old_flight.crew[crew]
            
            with open(self.file_name_upcoming, 'a', newline='', encoding="utf-8") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(row_dict)

        with open(self.file_name_upcoming, 'a', newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(writewrow_dict)
            


    def read_all_flight_nr(self):
        """Returns a list of all flight numbers"""
        flight_nrs = []

        with open(self.file_name_upcoming, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                flight_nrs.append(row["flight_nr"])
        return flight_nrs


    def update_flight(self, flight_to_update):
        flights = self.read_all_upcoming_flights()

        with open(self.file_name_upcoming, 'w', newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writeheader()

        for flight in flights:
            if flight.flight_nr == flight_to_update.flight_nr:
                flight = flight_to_update
            self.register_flight(flight)


    def get_fa_amount(self, filename):
        """Gets amount of flight attendant rows"""
        with open(filename, "r", newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            return [col for col in reader.fieldnames if col.startswith("fa")]


