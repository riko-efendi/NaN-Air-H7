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
            if user_input == "q":
                print("Quitting")
                break
            elif user_input == "2":
                destinations = self.logic_wrapper.get_all_destinations()
                print()
                print("[All Destinations]")
                print()
                for index, destination in enumerate(destinations):
                    print(f"{index+1:>2}.{' name: ':^2}{destination.airport:<}, {'Airport: '}{destination.name}, {destination.numeric_id}")
            else:
                print("Invalid")