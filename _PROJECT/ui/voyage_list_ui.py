from utils.ui_utils import UIUtils

from logic.logic_wrapper import LogicWrapper

from model.voyage import Voyage

from ui.input_validation import validate_date_format, validate_date_range, DateRangeError


class VoyageListUI:
    def __init__(self, logic_connection:LogicWrapper) -> None:
        self.ui_utils = UIUtils()
        self.logic_wrapper = logic_connection
        self.input_prompt_str = "Enter your choice: "

    def menu_output(self) -> None:
        """Prints out the options for the Voyage UI"""

        self.ui_utils.clear_screen()
        print(f"[LIST VOYAGES]\n")
        print(f"1. List Upcoming Voyages")
        print(f"2. List Past Voyages")
        print(f"3. List Voyage by date")
        print(f"4. List Voyage by week")

        print(f"\n[B]ack")

    def input_prompt(self) -> None:
        """Takes in an input from user, and jumpst to a specific UI/function based on that input."""

        user_input = ""

        while user_input != "b":
            self.menu_output()
            user_input = input("\n" + self.input_prompt_str).lower()

            if user_input == "1":
                upcoming_voyages = self.logic_wrapper.get_upcoming_voyages()
                self.ui_utils.print_voyages(upcoming_voyages, "[UPCOMING VOYAGES]")
                input("Press [ENTER] to exit: ")
                self.input_prompt_str = "Enter your choice: "
            
            elif user_input == "2":
                voyages = self.logic_wrapper.get_past_voyages()
                self.ui_utils.print_voyages(voyages, "[PAST VOYAGES]")
                input("Press [ENTER] to exit: ")
                self.input_prompt_str = "Enter your choice: "

            elif user_input == "3":
                self.list_voyage_by_date()

            elif user_input == "4":
                self.list_voyage_by_week()

            else:
                self.input_prompt_str = "Invalid. Enter another choice: "

    def list_voyage_by_date(self):
        """Gets date as input from user, and lists all voyages on that date"""

        self.ui_utils.clear_screen()
        user_input = input("Enter a date YYYY-MM-DD: ")
        while True:
            try:
                validate_date_format(user_input)
                break
            except ValueError:
                self.ui_utils.clear_screen()
                user_input = input("Wrong Format. Enter a date YYYY-MM-DD: ")

        voyages = self.logic_wrapper.get_voyages_of_date(user_input)
        self.ui_utils.print_voyages(voyages, f"[VOYAGES FLYING ON {user_input}]")
        input("Press [ENTER] to exit: ")
        self.input_prompt_str = "Enter your choice: "

    
    def list_voyage_by_week(self):
        start_date = input("Enter a start date YYYY-MM-DD: ")
        while True:
            try:
                validate_date_format(start_date)
                break
            except ValueError:
                self.ui_utils.clear_screen()
                start_date = input("Wrong Format. Enter a date YYYY-MM-DD: ")

        end_date = input("Enter an end date YYYY-MM-DD: ")
        
        while True:
            try:
                validate_date_range(start_date, end_date)
                break
            except ValueError:
                self.ui_utils.clear_screen()
                end_date = input("Wrong Format. Enter a date YYYY-MM-DD: ")
            except DateRangeError:
                self.ui_utils.clear_screen()
                end_date = input("The end date is ahead of start date. Enter a date YYYY-MM-DD: ")


        
        