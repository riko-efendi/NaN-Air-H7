class FlightLogic:
    def init(self, data_connection) -> None:
        self.data_wrapper = data_connection

    def get_all_upcoming_flights(self):
        return self.inject_destinations_to_flight(self.data_wrapper.get_all_upcoming_flights())

    def get_all_past_flights(self):
        return self.inject_destinations_to_flight(self.data_wrapper.get_all_past_flights())

    def inject_destinations_to_flight(self, flights):
        destinations = self.data_wrapper.get_all_destinations()

        for flight in flights:
            for destination in destinations:
                if destination.id.strip() == flight.dep_from.strip():
                    flight.depart_dest = destination

                elif destination.id.strip() == flight.arr_at.strip():
                    flight.arr_dest = destination


        return flights

    def print_upcoming_flights(self):
        self.print_flights(self.get_all_upcoming_flights())

    def print_past_flights(self):
        self.print_flights(self.get_all_past_flights())

    def print_flights(self, flights):
        for flight in flights:
            print(flight)