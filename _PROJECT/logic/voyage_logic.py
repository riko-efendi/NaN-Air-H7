from model.voyage import Voyage

class VoyageLogic:
    def __init__(self, data_connection) -> None:
        self.wrapper = data_connection

    def get_all_past_voyages(self):
        past_flights = self.wrapper.get_all_past_flights()
        past_voyages = []

        for index in range(0, len(past_flights), 2):
            flight_1 = past_flights[index]
            flight_2 = past_flights[index + 1]
            past_voyages.append(Voyage(flight_1, flight_2))

        return past_voyages

    def read_past_voyages(self):
        return self.wrapper.read_past_voyages()
    
    def get_all_upcoming_voyages(self):
        past_flights = self.wrapper.get_all_upcoming_flights()
        past_voyages = []

        for index in range(0, len(past_flights), 2):
            flight_1 = past_flights[index]
            flight_2 = past_flights[index + 1]
            past_voyages.append(Voyage(flight_1, flight_2))

        return past_voyages
    