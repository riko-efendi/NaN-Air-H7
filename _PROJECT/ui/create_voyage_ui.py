from utils.ui_utils import UIUtils
from model.voyage import Voyage



class CreateVoyageUI:
    def __init__(self, wrapper) -> None:
        self.logic_wapper = wrapper
        self.ui_utils = UIUtils
    def menu_output():
        header = f"[CREATING VOYAGES]"
        """We start by giving the user 2 options of either creating or editing the voyage"""
        print()
        print(header)
        print()
        print(f"1. Create new voyage")
        print(f"2. Edit voyage")

    
    def input_promt(self):
        while True: 
            self.menu_output()
            user_input =  input("\nEnter your choice: ").lower()
            # Clears screen ==> self.ui_utils.clear_screen() m  