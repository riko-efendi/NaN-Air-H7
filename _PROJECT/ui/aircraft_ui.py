

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
        print(f"q. Quit")

    def input_prompt(self):
        """This takes the input of the user"""
        while True:
            self.menu_output()
            user_input = input("\nEnter your choice: ").lower()
            if user_input == "q":
                print("Quitting")
                break
            elif user_input == "1":
                pass
            elif user_input == "2":
                pass
            else:
                print("Invalid")