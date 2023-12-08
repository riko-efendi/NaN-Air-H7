from utils.ui_utils import UIUtils
from model.voyage import Voyage

class CreateVoyageUI():
    def __init__(self, wrapper) -> None:
        self.logic_wrapper = wrapper

    def create_voyage(self, voyage):
        """Creates a voyage"""

        print("\n[CREATE VOYAGE]\n")
        self.flight_out = input("Input the flight out: ")
        self.flight_in = input("Input the flight in: ")
        self.pilot = input("Input the pilot: ")
        self.cabincrew = input("Input the cabin crew: ")
        #Add crew(optional?)

        print(f"\n{self.flight_out}-{self.flight_in} is successfully created.")
