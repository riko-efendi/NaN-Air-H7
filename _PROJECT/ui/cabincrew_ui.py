from logic.logic_wrapper import LogicWrapper


class CabinCrewUI:
    def __init__(self, wrapper) -> None:
       self.logic_wrapper = LogicWrapper()

    def menu_output(self):
        header = f"[PILOTS]"
        
        print()
        print(header)
        print()
        print(f"1. Register cabin crew")
        print(f"2. List All cabin crews")
        print(f"3. View specific cabin crew")
        print(f"q. Quit")

    def input_prompt(self):
        """ Takes in input from user """
        while True:
            self.menu_output()
            user_input = input("\nEnter your choice: ").lower()
            if user_input == "q":
                print("Quitting")
                break
            elif user_input == "2":
                cabincrews = self.logic_wrapper.get_all_cabincrews()
                print()
                print("[All Pilots]\n")
                for index, cabincrew in enumerate(cabincrews):
                    print(f"{index+1:>2}.{' Name: ':^2}{cabincrew.name:<}, {'Role: '}{cabincrew.role}")