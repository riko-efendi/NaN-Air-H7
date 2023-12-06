import csv

from model.voyage import Voyage

class VoyageData:
    def __init__(self) -> None:
        self.file_name = "_PROJECT/files/voyages.csv"

    def read_all_voyages(self):
        """Reads names and info from the "voyages.csv" file, and returns a list containing that information."""

        voyage_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                voyage_list_list.append(Employee(row["name"], row["flight out"], row["flight in"]))
        return voyage_list
    

    def create_voyage(self, voyage):

        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["name", 
                          "flight out", 
                          "flight in"] 
                          
            
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"name": voyage.name, "flight out": voyage.flight_out, "flight in": voyage.flight_in})
