from logic.logic_wrapper import LogicWrapper

class DestinationUI:
    def __init__(self, wrapper) -> None:
        self.logic_wrapper = wrapper

    def menu_output(self):
        header = f"[Destination]"

        print()
        print(header)
        print()
        print(f"1. Register Destination")
        print(f"2. List all destinations")
        print(f"b. Back")

    def input_prompt(self):
        while True:
            self.menu_output()
            user_input = input("\nEnter your choice: ").lower()
            if user_input == "b":
                return
            if user_input == "q":
                print("Quitting")
                break
            else:
                print("Invalid")