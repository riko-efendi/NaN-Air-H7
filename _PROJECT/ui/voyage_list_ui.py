from utils.ui_utils import UIUtils
from utils.logic_utils import LogicUtils
from logic.logic_wrapper import LogicWrapper
from ui.input_validation import validate_date_format, validate_date_range, DateRangeError

DASH_AMOUNT = 46

class VoyageListUI:
    def __init__(self, logic_connection:LogicWrapper) -> None:
        self.ui_utils = UIUtils()
        self.logic_utils = LogicUtils()
        self.logic_wrapper = logic_connection
        self.input_prompt_str = "Enter your choice: "

    def menu_output(self) -> None:
        """Prints out the options for the Voyage UI"""
        header = "[List Voyages]"
        self.ui_utils.clear_screen()
        print(header + "-" * (DASH_AMOUNT - len(header)) + "\n")
        print("\n" * 2)
        print(f"\t1. List Upcoming Voyages\n")
        print(f"\t2. List Past Voyages\n")
        print(f"\t3. List Voyage by date\n")
        print(f"\t4. List Voyage by date range\n")
        print("\n" * 2)
        print(f"\t\t\t\t\t[B]ack")
        print("-" * DASH_AMOUNT)

    def input_prompt(self) -> None:
        """Takes in an input from user, and jumpst to a specific UI/function based on that input."""

        user_input = ""

        while user_input != "b":
            self.menu_output()
            user_input = input("\n" + self.input_prompt_str).lower()

            if user_input == "1":
                upcoming_voyages = self.logic_wrapper.get_upcoming_voyages()
                self.ui_utils.print_voyages(upcoming_voyages, "[All Upcoming Voyages]")
                print("-" * DASH_AMOUNT + "\n")
                input("Press \033[34m[ENTER]\033[0m to exit: ")
                self.input_prompt_str = "Enter your choice: "
            
            elif user_input == "2":
                voyages = self.logic_wrapper.get_past_voyages()
                self.ui_utils.print_voyages(voyages, "[All Past Voyages]")
                print("-" * DASH_AMOUNT + "\n")
                input("Press \033[34m[ENTER]\033[0m to exit: ")
                self.input_prompt_str = "Enter your choice: "

            elif user_input == "3":
                self.list_voyage_by_date()
                self.input_prompt_str = "Enter your choice: "

            elif user_input == "4":
                self.list_voyage_by_week()
                self.input_prompt_str = "Enter your choice: "

            else:
                self.input_prompt_str = "\033[31mInvalid.\033[0m Enter another choice: "

            

    def list_voyage_by_date(self):
        """Gets date as input from user, and lists all voyages on that date"""
        header = "[View Voyages by Date]"
        self.ui_utils.clear_screen()
        print(header + "-" * (DASH_AMOUNT - len(header)) + "\n")
        print("\n" * 13)
        print(f"\t\t\t\t\t[B]ack")
        print("-" * DASH_AMOUNT + "\n")
        user_input = input("Enter a date YYYY-MM-DD: ").lower()
        while True:
            if user_input == 'b':
                    return None
            try:
                validate_date_format(user_input)
                break
            except ValueError:
                # self.ui_utils.clear_screen()
                user_input = input("\033[31mWrong Format.\033[0m Enter a date YYYY-MM-DD: ")

        voyages = self.logic_wrapper.get_voyages_of_date([user_input])
        self.ui_utils.print_voyages(voyages, f"[VOYAGE(S) ON {user_input}]")
        print("-" * DASH_AMOUNT + "\n")
        input("Press \033[34m[ENTER]\033[0m to exit: ")
        self.input_prompt_str = "Enter your choice: "

    
    def list_voyage_by_week(self):
        header = "[View Voyages by Week]"
        self.ui_utils.clear_screen()
        print(header + "-" * (DASH_AMOUNT - len(header)) + "\n")
        print("\n" * 13)
        print(f"\t\t\t\t\t[B]ack")
        print("-" * DASH_AMOUNT + "\n")
        start_date = input("Enter a start date YYYY-MM-DD: ").lower()
        while True:
            if start_date == 'b':
                return None
            try:
                validate_date_format(start_date)
                break
            except ValueError:
                # self.ui_utils.clear_screen()
                start_date = input("\033[31mWrong Format.\033[0m Enter a date YYYY-MM-DD: ")
                

        end_date = input("\nEnter an end date YYYY-MM-DD: ").lower()
        
        while True:
            if end_date == 'b':
                return None
            try:
                validate_date_range(start_date, end_date)
                break
            except ValueError:
                # self.ui_utils.clear_screen()
                end_date = input("\033[31mWrong Format.\033[0m Enter a date YYYY-MM-DD: ")
            except DateRangeError:
                # self.ui_utils.clear_screen()
                end_date = input("\033[31mThe end date can't be before the start date.\033[0m Enter a date YYYY-MM-DD: ")

        dates = self.logic_utils.generate_date_range(start_date, end_date)
        voyages = self.logic_wrapper.get_voyages_of_date(dates)
        self.ui_utils.print_voyages(voyages, f"[Voyage(s) between {start_date} - {end_date}]")
        print("-" * DASH_AMOUNT + "\n")
        input("Press \033[34m[ENTER]\033[0m to exit: ")
        self.input_prompt_str = "Enter your choice: "


        


        
        