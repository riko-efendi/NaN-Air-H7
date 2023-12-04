from logic.logic_wrapper import LogicWrapper

#from funclibrary.functions import clear_screen


class VoyageUI:
    def __init__(self, wrapper) -> None:
        self.logic_wrapper = wrapper

    def menu_output(self):
        header = f"[VOYAGE]"
        
        print()
        print(header)
        print()
        print(f"1. Create Voyage")
        print(f"2. List Voyage")
        print(f"3. Destination")
        print(f"4. Flight")
        print(f"5. Aircraft")
        print(f"q. Quit")

    def input_prompt(self):
        while True:
            self.menu_output()
            user_input = input("\nEnter your choice: ").lower()
            if user_input == "q":
                print("Quitting")
                break
            else:
                print("Invalid")
