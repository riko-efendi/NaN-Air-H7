import csv

from model.destination import Destination

class DestinationData:
    def __init__(self) -> None:
        self.file_name = "_PROJECT/files/destinations.csv"
        self.fieldnames = ["id", "destination", "numeric_id", "flight_time_from_kef"]

    def read_all_destinations(self):
        destination_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                destination_list.append(Destination(row["id"], row["destination"], row["numeric_id"], row["flight_time_from_kef"]))
        return destination_list
    
    def register_destination(self, destination:Destination):
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)

            writer.writerow({'id': destination.id, 'destination': destination.destination, 'numeric_id': destination.numeric_id, "flight_time_from_kef": destination.flight_time_from_kef})