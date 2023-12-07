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
                
            elif user_input == "b":
                break

            else:
                self.input_string = "Invalid. Enter another choice: "

            
