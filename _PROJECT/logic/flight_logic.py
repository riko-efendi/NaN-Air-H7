class FlightLogic:
    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection

    def get_all_upcoming_flights(self):

        self.inject_destinations_to_flight(self.data_wrapper.get_all_upcoming_flights())
        return self.data_wrapper.get_all_upcoming_flights()

    def get_all_past_flights(self):

        self.inject_destinations_to_flight(self.data_wrapper.get_all_past_flights())
        return self.data_wrapper.get_all_past_flights()

    def inject_destinations_to_flight(self, flights):

        destinations = self.data_wrapper.get_all_destinations()

        for flight in flights:
            for destination in destinations:
                if destination.id == flight.dep_from:
                    flight.dep_dest = destination
                elif destination.id == flight.arr_to:
                    flight.arr_dest == destination

        return None
