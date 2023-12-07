from utils.ui_utils import UIUtils

class ListEmployeeUI:
    def __init__(self, wrapper) -> None:
        self.logic_wrapper = wrapper
        self.ui_utils = UIUtils()

    def menu_output(self):

        print(f"[View Employee Options]\n")
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
                self.ui_utils.clear_screen()
                kennitala_input = input("Enter Employee' Kennitala: ")
                employee = self.logic_wrapper.get_employee_by_nid(kennitala_input)
                employee_name = employee.name
                self.print_employee(employee)
                
                print("[U]pdate Info\t[W]ork Schedule")
                option_input = input("Enter your command: ").lower()

                if option_input == "u":
                    print("[UPDATE EMPLOYEE INFO]\n")
                    new_address = input("New Address or press [K] to keep old address: ")
                    new_phone_number = input("New Phone Number or press [K] to keep old phone number: ")
                    self.logic_wrapper.update_employee_info(employee_name, kennitala_input, new_address, new_phone_number)
                    
                if option_input == "w":
                    self.ui_utils.clear_screen()
                    print("Insert beautiful work schedule here")
                    input("Press [ENTER] to exit")
            else:
                print("Invalid")


    def print_employee(self, employee):
        print(f"""Name: {employee.name}
Kt: {employee.print_kennitala}
Address: {employee.address}
Role: {employee.role}
Rank: {employee.rank}
""")
    
