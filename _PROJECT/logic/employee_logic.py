from data.employee_data import EmployeeData
from logic.aircraft_logic import AircraftLogic
from model.employee import Employee
from model.aircraft import Aircraft

class EmployeeLogic:
    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection

    def get_all_employees(self):
        return self.data_wrapper.get_all_employees()
    
    def get_employee_by_nid(self, kennitala):
        for employee in self.data_wrapper.get_all_employees():
            if kennitala == employee.kennitala:
                print(f"\nShowing result for {kennitala}\n")
                return f"""Name: {employee.name}
Kt: {employee.print_kennitala}
Address: {employee.address}
Role: {employee.role}
Rank: {employee.rank}
"""
            else:
                return f"\nNo Result for '{kennitala}'"
            
    def update_employee_info(self, kennitala, address, phone_number):
        employee = self.data_wrapper.get_employee_by_nid(kennitala)
        new_address = input("New Address or press [K] to keep old address: ")
        new_phone_number = input("New Phone Number or press [K] to keep old phone number: ")
        if new_address != "K":
            address = new_address
            return f"{self.employee.address}'s Address is updated successfully."
        if new_phone_number != "K":
            phone_number = new_phone_number
            return f"{self.employee.phone_number}'s Phone Number is updated successfully."

    def register_employee(self, employee):
        return self.data_wrapper.register_employee(employee)

    def get_all_pilots(self):
        return self.data_wrapper.get_all_pilots()
    
    def get_all_cabincrews(self):
        return self.data_wrapper.get_all_cabincrews()
    
    def get_all_pilots_by_license(self, license):
        return self.data_wrapper.get_all_pilots_by_license(license)
        # license_pilot_list = [] 
        # for pilot in self.data_wrapper.get_all_pilots():
        #     for aircraft in self.data_wrapper.get_all_aircrafts():
        #         if plane_type == aircraft.plane_type_id:
        #             license_pilot_list.append(pilot.name)
        # return license_pilot_list
                    