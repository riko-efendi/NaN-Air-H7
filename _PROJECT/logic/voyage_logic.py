from model.voyage import Voyage
from data.data_wrapper import DataWrapper
from utils.logic_utils import LogicUtils

class VoyageLogic:
    def __init__(self, data_connection:DataWrapper) -> None:
        self.wrapper = data_connection
        self.logic_utils = LogicUtils()
        

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
    

    def get_voyages_of_date(self, dates):
        """Takes in a list of dates and returns voyages that are flying during that date"""
        
        voyages_of_date = []
        voyages = self.get_all_voyages()
        for date in dates:
            for voyage in voyages:
                voyage_dates = self.logic_utils.generate_date_range(voyage.depart_date, voyage.arr_date)
                if date in voyage_dates:
                    voyages_of_date.append(voyage)

        return voyages_of_date

    def get_available_voyages_by_date(self, date):
        """Returns a list of flights available for an inputed date"""

        all_voyages = self.get_all_voyages()
        voyages_on_date = [] 

        for voyage in all_voyages:
            if date in self.logic_utils.generate_date_range(voyage.depart_date, voyage.arr_date):
                voyages_on_date.append(voyage)

        return voyages_on_date
    
    def get_non_available_voyages_by_date(self, date):
        """Returns a list of flights not available for an inputed date"""

        all_voyages = self.get_all_voyages()
        voyages_not_on_date = [] 

        for voyage in all_voyages:
            if date not in self.logic_utils.generate_date_range(voyage.depart_date, voyage.arr_date):
                voyages_not_on_date.append(voyage)

        return voyages_not_on_date


