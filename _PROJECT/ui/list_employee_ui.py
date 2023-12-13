from utils.ui_utils import UIUtils
from logic.logic_wrapper import LogicWrapper
from ui.input_validation import LengthERROR, DateError, validate_kennitala, validate_address,validate_phone_number, validate_input_view_by_kt, validate_year_format

class ListEmployeeUI:
    def __init__(self, logic_connection:LogicWrapper) -> None:
        self.logic_wrapper = logic_connection
        self.ui_utils = UIUtils()
        self.input_prompt_str = "Enter your choice: "

    def menu_output(self) -> None:
        """Prints out the options for the Employee Options Menu UI"""

        self.ui_utils.clear_screen()
        print(f"[VIEW EMPLOYEE OPTIONS]\n")
        print(f"1. View all employees")
        print(f"2. View Employee By Kennitala")
        print(f"3. View Off Duty Employees")
        print(f"4. View On Duty Employees")
        print(f"\n[B]ack")

    def input_prompt(self) -> None:
        """"Takes in an input from user, and jumpst to a specific UI/function based on that input."""

        user_input = ""

        while user_input != "b":
            self.menu_output()
            user_input = input("\n" + self.input_prompt_str).lower()
            if user_input == "1":
                self.view_all_employees()
                
            elif user_input == "2":
                self.view_employee_by_kennitala()

            elif user_input == "3":
                self.view_all_absent_employees()

            elif user_input == "4":
                self.view_employees_past_schedule_by_date()

            else:
                self.input_prompt_str = "Invalid. Enter another choice: "

    def view_all_employees(self) -> None:
        """Prints out every employee registered in the crew.csv file."""

        employees = self.logic_wrapper.get_all_employees()
        self.ui_utils.clear_screen()
        print("[ALL EMPLOYEES]\n")
        for index, employee in enumerate(employees):
            print(f"{index+1:>2}.{' name: ':^2}{employee.name:<}, {employee.role}\n      {'kt: ' + employee.print_kennitala}")
        input("\nPress [ENTER] to exit: ")


    def print_update_employee_info(self, name, kennitala, address, role, rank, phone_number):
        self.ui_utils.clear_screen()
        print("[UPDATE EMPLOYEE INFO]\n")
        self.print_employee(name, kennitala, address, role, rank, phone_number)


    def print_employee(self, name, kennitala, address, role, rank, phone_number) -> None:
        print(f"Name: {name}")
        print(f"Kt: {kennitala}")
        print(f"Address: {address}")
        print(f"Role: {role}")
        print(f"Rank: {rank}")
        print(f"Phone number: {phone_number}")

    def view_employee_by_kennitala(self):
        self.ui_utils.clear_screen()
        #first we have to make sure the user ONLY puts a valid kennitala and see if the user inputs
        #the right values for the kennitala
        while True:
            try:
                kennitala_input = input("Enter Employee Kennitala: ")
                self.ui_utils.clear_screen()
                validate_kennitala(kennitala_input)
                employee = self.logic_wrapper.get_employee_by_nid(kennitala_input)
                if employee != None:
                    break
                else:
                    print("Employeee not found")

            except ValueError:
                print("invalid value, please enter a valid kennitala")
            except LengthERROR:
                print("Invalid length, please enter a valid kennitala")
        
        self.ui_utils.clear_screen()
        print(f"[EMPLOYEE INFO]\n")
        self.print_employee(employee.name, employee.kennitala, employee.address, employee.role, employee.rank, employee.phone_number)

        print("\n[U]pdate Info\t[W]ork Schedule\t  [B]ack\n")
        #this checks the option that the user inputs. usually if this wasnt here it would bring the user back to the previous
        #menu so I decided to add this to make sure the user choses the options that were given to them.
        while True:
            try:    
                option_input = input("Enter your choice: ").lower()
                validate_input_view_by_kt(option_input)
                break
            except ValueError:
                self.ui_utils.clear_screen()
                print(f"[EMPLOYEE INFO]\n")
                self.print_employee(employee.name, employee.kennitala, employee.address, employee.role, employee.rank, employee.phone_number)

                print("\n[U]pdate Info\t[W]ork Schedule\t  [B]ack\n")
                print("Invalid input.")

        if option_input == "u":
            self.ui_utils.clear_screen()
            self.print_update_employee_info(employee.name, employee.kennitala, employee.address, employee.role, employee.rank, employee.phone_number)
            print()
            #now if the user wishes to update the info they are given a couple of options.
            #first option is to change the address but the addres have to be somewhat valid with 
            #a street name first and then 2 numbers afterwards. this loop prevents them inputting something else
            #like numbers first and then letters later or the length of the address. 
            while True:
                try:
                    new_address = input("Enter a new address or [K]eep old address: ")
                    if new_address.lower() == "k":
                        new_address = employee.address
                    validate_address(new_address)
                    self.print_update_employee_info(employee.name, employee.kennitala, new_address.upper(), employee.role, employee.rank, employee.phone_number)
                    print()
                    break

                except ValueError:
                    self.ui_utils.clear_screen()
                    self.print_update_employee_info(employee.name, employee.kennitala, employee.address, employee.role, employee.rank, employee.phone_number)
                    print("\nInvalid values")

                except LengthERROR:
                    self.ui_utils.clear_screen()
                    self.print_update_employee_info(employee.name, employee.kennitala, employee.address, employee.role, employee.rank, employee.phone_number)
                    print("\nInvalid length")

            #this check prevents the user adding something random into the phone number
            #this validates then the phone number and checks if it fits the right amount of numbers 
            while True:
                try:
                    
                    new_phone_number = input("Enter a new phone number or [K]eep old phone number: ").lower()
                    if new_phone_number.lower() == "k":
                        new_phone_number = employee.phone_number
                    validate_phone_number(new_phone_number)
                    
                    break

                except ValueError:
                    self.ui_utils.clear_screen()
                    self.print_update_employee_info(employee.name, employee.kennitala, new_address.upper(), employee.role, employee.rank, employee.phone_number)
                    print("\nInvalid values, please only use numbers")
                except LengthERROR:
                    self.ui_utils.clear_screen()
                    self.print_update_employee_info(employee.name, employee.kennitala, new_address.upper(), employee.role, employee.rank, employee.phone_number)
                    print("\nInvalid number.")

            self.print_update_employee_info(employee.name, employee.kennitala, new_address.upper(), employee.role, employee.rank, new_phone_number.upper())
            self.logic_wrapper.update_employee_info(kennitala_input, new_address, new_phone_number)
            print("\nSuccess!")
            input("\nPress [ENTER] to confirm: ") 



        elif option_input == "w":
            self.view_work_schedule_by_week(employee.kennitala)     
        elif option_input == "b":
            return None
           
        

    def view_work_schedule_by_week(self, kennitala):
        self.ui_utils.clear_screen()
        print(f"[WORK SUMMARY]\n")
        while True:
            #this loops is repeated in the following loooops this is to just make sure the user inputs a valid date and if the date makes sense
            #it will let them continue. 
            try:
                start_date = input("Enter Date [YYYY-MM-DD]: ")
                self.ui_utils.clear_screen()
                validate_year_format(start_date)
                break
            except ValueError:
                print("Invalid date, please only use digits")
            except LengthERROR:
                print("Invalid date, pleasa use format [YYYY-MM-DD]")
            except DateError:
                print("Invalid date, month and/or day does not exist")

        while True:
            try:
                end_date = input("Enter Date [YYYY-MM-DD]: ")
                validate_year_format(start_date)
                break
            except ValueError:
                print("Invalid date, please only use digits")
            except LengthERROR:
                print("Invalid date, pleasa use format [YYYY-MM-DD]")
            except DateError:
                print("Invalid date, month and/or day does not exist")

        flights = self.logic_wrapper.get_employees_past_schedule_by_date_range_and_kennitala(start_date, end_date, kennitala)
        employee = self.logic_wrapper.get_employee_by_nid(kennitala)
        
        self.ui_utils.clear_screen()
        print(f"Work Schedule for {employee.name} from {start_date} to {end_date}\n")

        if flights:
            for flight in flights:
                print(f"Flight Number: {flight['flight_nr']}, From: {flight['dep_from']} To: {flight['arr_at']}, Departure: {flight['departure_date']} {flight['departure_time']}, Arrival: {flight['arrival_date']} {flight['arrival_time']}")
        else:
            print("No flights scheduled for this employee within the specified date range.")

        input("\nPress [ENTER] to exit: ")

    def view_employees_past_schedule_by_date(self):
        self.ui_utils.clear_screen()
        while True:
            try:
                date_input = input("Enter Date [YYYY-MM-DD]: ")
                self.ui_utils.clear_screen()
                validate_year_format(date_input)
                break
            except ValueError:
                print("Invalid date, please only use digits")
            except LengthERROR:
                print("Invalid date, please use format [YYYY-MM-DD]")
            except DateError:
                print("Invalid date, month and/or day does not exist")

        flights = self.logic_wrapper.get_employees_past_schedule_by_date(date_input)
        self.ui_utils.clear_screen()
        print(f"ALL ON DUTY EMPLOYEES on {date_input}\n")

        employees_printed = set() 

        for flight in flights:
            unique_employees = {flight.captain, flight.copilot, flight.fsm, flight.fa1, flight.fa2}

            for employee_nid in unique_employees:
                if employee_nid not in employees_printed:
                    employee = self.logic_wrapper.get_employee_by_nid(employee_nid)
                    if employee: 
                        print(f"{employee.name}, \tDestination: {flight.arr_at}")
                    employees_printed.add(employee_nid) 

        input("\nPress [ENTER] to exit: ")

    def view_all_absent_employees(self):
        self.ui_utils.clear_screen()
        while True:
            try:
                date_input = input("Enter Date [YYYY-MM-DD]: ")
                self.ui_utils.clear_screen()
                validate_year_format(date_input)
                break
            except ValueError:
                print("Invalid date, please only use digits")
            except LengthERROR:
                print("Invalid date, pleasa use format [YYYY-MM-DD]")
            except DateError:
                print("Invalid date, month and/or day does not exist")


        all_employees = set(employee.kennitala for employee in self.logic_wrapper.get_all_employees())


        on_duty_employees = set()
        flights = self.logic_wrapper.get_employees_past_schedule_by_date(date_input)
        for flight in flights:
            on_duty_employees.update({flight.captain, flight.copilot, flight.fsm, flight.fa1, flight.fa2})
        
        absent_employees = all_employees - on_duty_employees  

        self.ui_utils.clear_screen()
        print(f"Off Duty Employees on {date_input}:\n")
        for employee_nid in absent_employees:
            employee = self.logic_wrapper.get_employee_by_nid(employee_nid)
            if employee:
                print(f"{employee.name}, \tRole: {employee.rank}")

        input("\nPress [ENTER] to exit: ")