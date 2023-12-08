from logic.logic_wrapper import LogicWrapper
from model.aircraft import Aircraft

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

            if user_input == "2":
                aircrafts = self.logic_wrapper.get_all_aircrafts()
                print("[All Aircrafts]\n")
                for index, aircraft in enumerate(aircrafts):
                    print(f"{index+1:>2}. {'Plane Insignia':^2}{aircraft.plane_insignia:<}, {'Plane Type id: '}{aircraft.plane_type_id}, {'DOM: '}{aircraft.date_of_manufacture}, {'Last Maintenance: '}{aircraft.last_maintenance}")
                input("\nPress [ENTER] to exit: ")
            else:
                print("Invalid")