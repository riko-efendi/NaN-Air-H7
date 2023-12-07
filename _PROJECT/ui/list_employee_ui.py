from utils.ui_utils import UIUtils

class ListEmployeeUI:
    def __init__(self, wrapper) -> None:
        self.logic_wrapper = wrapper
        self.ui_utils = UIUtils()

    def menu_output(self):
        self.ui_utils.clear_screen()
        print(f"[VIEW EMPLOYEE OPTIONS]\n")
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
                self.view_employee_by_kennitala()

            else:
                print("Invalid")

    def print_update_employee_info(self, name, kennitala, address, role, rank, phone_number):
        self.ui_utils.clear_screen()
        print("[UPDATE EMPLOYEE INFO]\n")
        self.print_employee(name, kennitala, address, role, rank, phone_number)

    def print_employee(self, name, kennitala, address, role, rank, phone_number):
        self.ui_utils.clear_screen()
        print(f"[EMPLOYEE INFO]\n")
        print(f"Name: {name}")
        print(f"Kt: {kennitala}")
        print(f"Address: {address}")
        print(f"Role: {role}")
        print(f"Rank: {rank}")
        print(f"Phone number: {phone_number}")

    def view_employee_by_kennitala(self):
        self.ui_utils.clear_screen()
        kennitala_input = input("Enter Employee Kennitala: ")
        employee = self.logic_wrapper.get_employee_by_nid(kennitala_input)
        self.print_employee(employee.name, employee.kennitala, employee.address, employee.role, employee.rank, employee.phone_number)

        print("\n[U]pdate Info\t[W]ork Schedule")
        option_input = input("\nEnter your command: ").lower()

        if option_input == "u":
            self.print_update_employee_info(employee.name, employee.kennitala, employee.address, employee.role, employee.rank, employee.phone_number)

            new_address = input("\nNew Address or press [K] to keep old address: ")
            if new_address.lower() == "k":
                new_address = employee.address

            self.print_update_employee_info(employee.name, employee.kennitala, new_address.upper(), employee.role, employee.rank, employee.phone_number)

            new_phone_number = input("\nNew Phone Number or press [K] to keep old phone number: ").lower()
            if new_phone_number.lower() == "k":
                new_phone_number = employee.phone_number

            self.print_update_employee_info(employee.name, employee.kennitala, new_address.upper(), employee.role, employee.rank, new_phone_number.upper())

            self.logic_wrapper.update_employee_info(kennitala_input, new_address, new_phone_number)

            print("\nSuccess!")

            input("\nPress [ENTER] to confirm: ")
            
        elif option_input == "w":
            self.ui_utils.clear_screen()
            print(f"[WORK SCHEDULE]\n")
            print("Insert beautiful work schedule here")
            input("Press [ENTER] to exit")