import csv

#from model.employee import Employee
#from model.flight import Flight

from model.voyage import Voyage

class VoyageData():
    def __init__(self) -> None:
        self.file_name = "voyages.csv"

    def get_all_voyages():
        pass

    def create_new_voyage(self,voyage):
        """Writes a new creation of a voyage"""
        fieldnames = ["fid","flight_out","flight_in","pilot","cabincrew"]

        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"fid":voyage.fid,"flight_out":voyage.flights,"flight_in":voyage.flight, "pilot":voyage.pilot,"cabincrew":voyage.cabincrew})


    
        