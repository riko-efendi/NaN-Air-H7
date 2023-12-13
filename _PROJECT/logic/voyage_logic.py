from model.voyage import Voyage
from data.data_wrapper import DataWrapper
from utils.logic_utils import LogicUtils

class VoyageLogic:
    def __init__(self, data_connection:DataWrapper) -> None:
        self.wrapper = data_connection
        self.logic_util = LogicUtils()
        

    def get_all_past_voyages(self):
        past_flights = self.wrapper.get_all_past_flights()
        past_voyages = []

        for index in range(0, len(past_flights), 2):
            flight_1 = past_flights[index]
            flight_2 = past_flights[index + 1]
            past_voyages.append(Voyage(flight_1, flight_2))

        return past_voyages


    def get_all_upcoming_voyages(self):
        past_flights = self.wrapper.get_all_upcoming_flights()
        past_voyages = []

        for index in range(0, len(past_flights), 2):
            flight_1 = past_flights[index]
            flight_2 = past_flights[index + 1]
            past_voyages.append(Voyage(flight_1, flight_2))

        return past_voyages
    
    def get_all_voyages(self):
        upcoming_voyages = self.get_all_upcoming_voyages()
        past_voyagees = self.get_all_past_voyages()

        return upcoming_voyages + past_voyagees
    
    def update_voyage(self, voyage):
        return self.wrapper.update_voyage(voyage)
    

    def get_voyages_of_date(self, date):
        """Takes in a date and returns voyages that are flying during that date"""
        
        voyages_of_date = []
        voyages = self.get_all_voyages()

        for voyage in voyages:
            voyage_dates = self.logic_util.generate_date_range(voyage.depart_date, voyage.arr_date)
            if date in voyage_dates:
                voyages_of_date.append(voyage)

        return voyages_of_date
    

