from logic.logic_wrapper import LogicWrapper

class RegisterPilotUI:
    def __init__(self, wrapper) -> None:
       self.logic_wrapper = LogicWrapper()

    def menu_output(self):
        header = f"[REGISTER PILOT]"

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