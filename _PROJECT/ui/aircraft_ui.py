<<<<<<< HEAD
from logic.aircraft_logic import Aircraft
from model.aircraft import Aircraft
from utils.utils import UIUtils
=======
from logic.logic_wrapper import LogicWrapper
from model.aircraft import Aircraft
>>>>>>> 50f6add73441a8db699aaa422da6b0dfba2cce87

class AircraftUI:
    def __init__(self, wrapper) -> None:
        self.logic_wrapper = wrapper

    def menu_output(self):
        header = f"[Aircraft]"

        print()
        print(header)
        print()
        print(f"1. Register aircraft")
        print(f"2. List all aircrafts")
        print(f"\n[B]ack")

    def input_prompt(self):
        """This takes the input of the user"""
        while True:
            self.menu_output()
            user_input = input("\nEnter your choice: ").lower()
            if user_input == "b":
                break
<<<<<<< HEAD
            elif user_input == "1":
                pass
            elif user_input == "2":
                aircrafts = self.logic_wrapper.get_all_aircrafts()
                print()
                print()
                print()
                for index, aircrafts in enumerate(aircrafts):
                    print(f"{index+1:>2}.{' sign: ':^2} {aircrafts.sign}  plane type: {aircrafts.id} {'Date of Manufacture' :>12}: {aircrafts.manufacture} {'Last maintenance':>12} {aircrafts.maintenance}")
=======

            if user_input == "2":
                aircrafts = self.logic_wrapper.get_all_aircrafts()
                print("[All Aircrafts]\n")
                for index, aircraft in enumerate(aircrafts):
                    print(f"{index+1:>2}. {'Plane Insignia':^2}{aircraft.plane_insignia:<}, {'Plane Type id: '}{aircraft.plane_type_id}, {'DOM: '}{aircraft.date_of_manufacture}, {'Last Maintenance: '}{aircraft.last_maintenance}")
                input("\nPress [ENTER] to exit: ")
>>>>>>> 50f6add73441a8db699aaa422da6b0dfba2cce87
            else:
                print("Invalid")