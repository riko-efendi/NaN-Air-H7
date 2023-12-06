
class ListEmployeeUI:
    def __init__(self, wrapper) -> None:
        self.logic_wrapper = wrapper

    def menu_output(self):
        header = f"[View Employee Options]"

        print()
        print(header)
        print()

        print(f"1. View all employees")
        print(f"2. View Employee By Kennitala")
        print(f"3. View Off Duty Employees")
        print(f"4. View On Duty Employees")
        print(f"q. Quit")

    def input_prompt(self):
        """ Takes in input from user """
        while True:
            self.menu_output()
            user_input = input("\nEnter your choice: ").lower()


            if user_input == "q":
                print("Quitting")
                break
            elif user_input == "1":
                employees = self.logic_wrapper.get_all_employees()
                print()
                print("[ALL EMPLOYEES]")
                print()
                for index, employee in enumerate(employees):
                    print(f"{index+1:>2}.{' name: ':^2}{employee.name:<}, {employee.role}\n      {'kt: ' + employee.print_kennitala}")
            elif user_input == "2":
                kennitala_input = input("Enter Employee' Kennitala: ")
                print(self.logic_wrapper.get_employee_by_nid(kennitala_input))
            else:
                print("Invalid")