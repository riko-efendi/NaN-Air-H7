class RegisterEmployeeUI():
    def __init__(self, wrapper) -> None:
        self.logic_wrapper = wrapper

    def register_employee(self, employee):
        """Registers an employee"""

        print("\n[REGISTER EMPLOYEE]\n")
        employee.name = input("Input the employee name: ")
        employee.kennitala = (input("Input the employee kennitala: "))
        e_role = ""
        while e_role != "1" and e_role != "2":
            e_role = input("Is the employee: 1. Pilot or 2. Cabincrew? 1/2: ").lower()
        if e_role == "1":
            employee.role = "Pilot"
        elif e_role == "2":
            employee.role = "Cabincrew"

        employee.address = input("Input the employees address: ")
        employee.phone_number = input("Input the employees phone number: ")
        self.logic_wrapper.register_employee(employee)
        print(f"\n{employee.name} is successfully created.")

    def register_pilot(self, employee):
        """Registers a pilot"""
        
        print("\n[REGISTER PILOT]\n")
        employee.name = input("Input the employee name: ")
        employee.kennitala = (input("Input the employee kennitala: "))
        employee.role = "Pilot"
        e_rank = ""
        while e_rank != "1" and e_rank != "2":
            e_rank = input("Is the employee: 1. Captain or 2. Copilot? 1/2: ").lower()
        if e_rank == "1":
            employee.rank = "Captain"
        elif e_rank == "2":
            employee.rank = "Copilot"

        employee.address = input("Input the employees address: ")
        employee.phone_number = input("Input the employees phone number: ")
        self.logic_wrapper.register_employee(employee)
        print(f"\n{employee.name} is successfully created.")


    def register_cabin_crew(self, employee):
        """Registers a cabin crew"""

        print("\n[REGISTER CABIN CREW]\n")
        employee.name = input("Input the employee name: ")
        employee.kennitala = (input("Input the employee kennitala: "))
        employee.role = "Cabincrew"
        e_rank = ""
        while e_rank != "1" and e_rank != "2":
            e_rank = input("Is the employee: 1. Flight Service Manager or 2. Flight Attendant? 1/2: ").lower()
        if e_rank == "1":
            employee.rank = "Flight Service Manager"
        elif e_rank == "2":
            employee.rank = "Flight Attendant"

        employee.address = input("Input the employees address: ")
        employee.phone_number = input("Input the employees phone number: ")
        self.logic_wrapper.register_employee(employee)
        print(f"\n{employee.name} is successfully created.")
        