class DestinationLogic:
    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection

    def get_all_destinations(self):
        return self.data_wrapper.get_all_destinations()
    
    def create_destination(self, destination):
        self.data_wrapper.create_destination(destination)
