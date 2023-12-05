from logic.logic_wrapper import LogicWrapper


class PilotUI:
    def __init__(self, wrapper) -> None:
       self.logic_wrapper = LogicWrapper()

    def menu_output(self):
        header = f"[PILOTS]"
        
        print()
        print(header)
        print()
        print(f"1. Register pilot")
        print(f"2. List pilots")
        print(f"3. View specific pilot")
        print(f"q. Quit")

    def input_prompt(self):
        """ Takes in input from user """
        while True:
            self.menu_output()
            user_input = input("\nEnter your choice: ").lower()

