from data.destination_data import DestinationData
from model.destination import Destination

class DestinationLogic:
    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection

    def get_all_destinations(self):
        return self.data_wrapper.get_all_destinations()