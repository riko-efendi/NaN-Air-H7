from utils.ui_utils import UIUtils

class ListEmployeeUI:
    def __init__(self, wrapper) -> None:
        self.logic_wrapper = wrapper
        self.ui_utils = UIUtils()

    def menu_output(self):
        header = f"[View Employee Options]"


        print(header)
        print()

        print(f"1. View all employees")
        print(f"2. View Employee By Kennitala")
        print(f"3. View Off Duty Employees")
        print(f"4. View On Duty Employees")
        print(f"\n[B]ack")

    def input_prompt(self):
        """ Takes in input from user """
        while True:
            self.menu_output()
            user_input = input("\nEnter your choice: ").lower()


            if user_input == "b":
                break

            elif user_input == "1":
                employees = self.logic_wrapper.get_all_employees()
                self.ui_utils.clear_screen()
                print("[ALL EMPLOYEES]\n")

                for index, employee in enumerate(employees):
                    print(f"{index+1:>2}.{' name: ':^2}{employee.name:<}, {employee.role}\n      {'kt: ' + employee.print_kennitala}")

                input("\nPress [ENTER] to exit: ")
            elif user_input == "2":
                kennitala_input = input("Enter Employee' Kennitala: ")
                print(self.logic_wrapper.get_employee_by_nid(kennitala_input))

                print("[U]pdate Info            [W]ork Schedule")
                option_input = input("Enter your command: ")
                if option_input == "U":
                    print("[UPDATE EMPLOYEE INFO]\n")
                    new_address = input("New Address or press [K] to keep old address: ")
                    new_phone_number = input("New Phone Number or press [K] to keep old phone number: ")
                    return self.logic_wrapper.update_employee_info(kennitala_input, new_address, new_phone_number)
            else:
                print("Invalid")

    
