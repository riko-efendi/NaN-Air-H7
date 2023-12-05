import csv

from model.destination import Destination

class DestinationData:
    def __init__(self) -> None:
        self.file_name = "_PROJECT/files/destination.csv"

    def read_all_destinations(self):
        destination_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                destination_list.append(Destination(row["id"], row["destination"], row["numeric_id"]))
        return destination_list