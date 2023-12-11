
from utils.ui_utils import UIUtils

class CreateVoyageUI():
    def __init__(self, wrapper) -> None:
        self.logic_wrapper = wrapper
        self.ui_utils = UIUtils()

    def create_voyage(self, voyage):
        """Creates a voyage"""
        self.ui_utils.clear_screen()
        print("\n[CREATE VOYAGE]\n")
        while True:
            flights = self.logic_wrapper.get_all_upcoming_flights()
            fid_dict = []
            for index, flights in enumerate(flights):
                fid_dict.append(flights.flight_nr)


            voyage.flight_out = input("Input the flight out:")
            voyage.flight_in = input("Input the flight in: ")
            #if there was a pilot :) 
            find_pilot = input("Input the pilot: ")
            pilots = self.logic_wrapper.get_all_pilots()
            voyage.name = ""
            for index, pilot in enumerate(pilots):
                if find_pilot == pilot.name:
                #then add this pilot to the csv file :) 
                    print("yes :)")
                    break
                elif find_pilot == "":
                    break
                else:
                    pass

            if voyage.name:
                print("")
                
            stop =input("press enter to continue")







    



        #cabincrew = input("Input the cabin crew: ")

        
        #if cabincrew != None:
        

        #Add crew(optional?)
        #self.logic_wrapper.create_voyage()
        #print(f"\n{voyage.flight_out}-{voyage.flight_in} is successfully created.")
