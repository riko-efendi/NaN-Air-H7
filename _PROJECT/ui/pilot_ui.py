from logic.logic_wrapper import LogicWrapper
from ui.register_pilot_ui import RegisterPilotUI


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
            # Clears screen
            # self.ui_utils.clear_screen()
            if user_input == "q":
                print("Quitting")
                break
            elif user_input == "1":
                register_pilot_menu = RegisterPilotUI(self.logic_wrapper)
                back_method = register_pilot_menu.input_prompt()
                if back_method == "q":
                    return "q"