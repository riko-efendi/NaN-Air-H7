from utils.ui_utils import UIUtils

from logic.logic_wrapper import LogicWrapper

from model.voyage import Voyage


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

        print(f"\n[B]ack")

    def input_prompt(self) -> None:
        """Takes in an input from user, and jumpst to a specific UI/function based on that input."""

        user_input = ""

        while user_input != "b":
            self.menu_output()
            user_input = input("\n" + self.input_prompt_str).lower()

            if user_input == "1":
                upcoming_voyages = self.logic_wrapper.get_upcoming_voyages()
                self.list_voyages(upcoming_voyages, "[UPCOMING VOYAGES]")
            
            if user_input == "2":
                past_voyages = self.logic_wrapper.get_past_voyages()
                self.list_voyages(past_voyages, "[PAST VOYAGES]")

            else:
                self.input_prompt_str = "Invalid. Enter another choice: "


    def list_voyages(self, voyages:list[Voyage], header:str=""):

        self.ui_utils.clear_screen()
        print(f"{header}\n")

        for voyage in voyages:
            print(voyage, end="\n\n")

        input("Press [ENTER] to exit: ")
