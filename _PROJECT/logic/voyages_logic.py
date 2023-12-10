from logic.logic_wrapper import LogicWrapper

class VoyageLogic:

    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper

    def create_voyage(self):
        self.logic_wrapper.get_all_upcoming_flights()
        

    