import csv
from model.voyage import Voyage
from data.flight_data import FlightData

class VoyageData():
    def __init__(self) -> None:
        self.flight_data = FlightData()
        self.file_name = "_PROJECT/files/upcoming_flights.csv"
        
    
    def update_voyage(self,voyage):
        self.flight_data.update_flight(voyage.flight_1)
        self.flight_data.update_flight(voyage.flight_2)
