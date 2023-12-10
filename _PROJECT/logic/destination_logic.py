from data.data_wrapper import DataWrapper
from model.destination import Destination

class DestinationLogic:
    def __init__(self, data_connection:DataWrapper) -> None:
        self.data_wrapper = data_connection

    def get_all_destinations(self, include_kef, as_dict) -> list[Destination]:
        """Returns all destinations, with an optional arguement to include KEF airport or not, and if you want it in a list or a dictionary"""
        destinations = self.data_wrapper.get_all_destinations()
        

        if not include_kef:
            for index, destination in enumerate(destinations):
                if destination.id != "KEF":
                    destinations.pop(index)
                    break
            
        destinations_dict = {index: value for index, value in enumerate(destinations)}
        return destinations_dict if as_dict else destinations
    
    def create_destination(self, destination):
        self.data_wrapper.create_destination(destination)

