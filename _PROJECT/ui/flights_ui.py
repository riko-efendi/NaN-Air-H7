from utils.ui_utils import UIUtils

class FlightsUI:
    def __init__(self, logic_connection) -> None:
        self.ui_utils = UIUtils()
        self.logic_wrapper = logic_connection
        self.input_string = "Enter your choice: "

    def menu_output(self):
        self.ui_utils.clear_screen()
        print(f"[FLIGHTS]\n")
        print(f"1. List Upcoming Flights")
        print(f"2. List Past Flights")
        print(f"3. Create Flight")
        print(f"4. List Flights From One Airport")
        print(f"\n[B]ack")
    
    def input_prompt(self):
        while True:
            self.menu_output()
            user_input = input("\n" + self.input_string).lower()

            if user_input == "1":
                self.ui_utils.clear_screen()
                print(f"[ALL UPCOMING FLIGHTS]\n")
                self.logic_wrapper.print_all_upcoming_flights()
                input("\nPress [ENTER] to exit: ")
            
            elif user_input == "2":
                self.ui_utils.clear_screen()
                print(f"[ALL PAST FLIGHTS]\n")
                self.logic_wrapper.print_all_past_flights()
                input("\nPress [ENTER] to exit: ")

            elif user_input == "4":
                self.ui_utils.clear_screen()
                
                airport_id = {
                    "1": "KEF",
                    "2": "LYR",
                    "3": "GOH",
                    "4": "KUS",
                    "5": "FAE",
                    "6": "LWK"
                }
                print("[Flight(s) List from Airport]\n")
                while True:
                    print("[Airport ID]\n\n1. KEF 2. LYR 3. GOH 4. KUS 5. FAE 6. LWK")
                    airport_id_input = input("\nEnter License Type (1, 2, 3, 4, 5, or 6): ")
                    if airport_id_input in airport_id:
                        airport_id_input = airport_id[airport_id_input]
                        break
                    else:
                        print("Invalid input. Please enter 1, 2, 3, 4, 5, or 6.")

                print(f"\nShowing flight(s) from {airport_id_input}\n")
                airport_flights = self.logic_wrapper.get_all_flights_from_one_airport(airport_id_input)
                for index, airport_flight in enumerate(airport_flights):
                    print(f"{index+1:>2}. {airport_flight}")
                input("\nPress [ENTER] to exit: ")

            elif user_input == "5":
                self.ui_utils.clear_screen()
                kennitala_input = input("Enter Employee Kennitala: ")
                print(f"\nShowing flight trip(s) for {kennitala_input}\n")
                schedules = self.logic_wrapper.get_employee_past_schedule_by_nid(kennitala_input)
                for index, schedule in enumerate(schedules):
                    print(f"{index+1:>2}. {schedule}\n")
                input("\nPress [ENTER] to exit: ")
                
            elif user_input == "b":
                break

            else:
                self.input_string = "Invalid. Enter another choice: "

            
