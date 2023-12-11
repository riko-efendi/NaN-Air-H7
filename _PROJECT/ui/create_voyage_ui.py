
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
            fid_list = [flight.flight_nr for flight in flights]

            while True: 
                #First we need a valid id for the first flight out(i need to somehow find a way as they
                # input the flight out code, there would be another individual list that are flights available to flight back in)
                voyage.flight_out = input("Input the flight out:")
                if voyage.flight_out in fid_list:
                    print("Valid ID!")
                    break
                else:
                    print("Please enter a valid ID.")
            #We iterate through the list of id (but i still need to somehow find the flights after 
            # they have inputed the first flight out. )
            while True:
                voyage.flight_in = input("Input the flight in:")
                if voyage.flight_in in fid_list:
                    print("Valid ID for flight in!")
                    break
                else:
                    print("Please enter a valid ID for flight in.")

            #if there was a pilot :) (This is optional)
            while True:

                find_pilot = input("Input the pilot: ")
                pilots = self.logic_wrapper.get_all_pilots()
                pilot_list = [pilot.name for pilot in pilots]
                
                if find_pilot in pilot_list or find_pilot == "":
                #then add this pilot to the csv file :) 
                    return
                else:
                    print("please enter a valid Pilot")








    



        #cabincrew = input("Input the cabin crew: ")

        
        #if cabincrew != None:
        

        #Add crew(optional?)
        #self.logic_wrapper.create_voyage()
        #print(f"\n{voyage.flight_out}-{voyage.flight_in} is successfully created.")
