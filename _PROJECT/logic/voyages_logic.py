from data.data_wrapper import DataWrapper
from model.voyage import Voyage

class VoyageLogic:

    def __init__(self, data_connection:DataWrapper) -> None:
        self.data_wrapper = data_connection

    def get_upcoming_voyages(self):
        """Returns a list of upcoming voyages, read from the upcoming_fligths.csv file"""

        upcoming_flights = self.data_wrapper.get_all_upcoming_flights()
        voyages = []

        for index in range(0,len(upcoming_flights), 2):
            voyages.append(Voyage(upcoming_flights[index], upcoming_flights[index + 1]))
        
        return voyages



    def get_past_voyages(self):
        """Returns a list of past voyages, read from the past_flights.csv file"""

        past_flights = self.data_wrapper.get_all_past_flights
        voyages = []

        for index in range(0,len(past_flights), 2):
            voyages.append(Voyage(past_flights[index], past_flights[index + 1]))
        
        return voyages

        

    