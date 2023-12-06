from model.employee import Employee

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
Role: {employee.role}
Rank: {employee.rank}
"""
            else:
                return f"\nNo Result for '{kennitala}'"
            
    def register_employee(self, employee):
        return self.data_wrapper.register_employee(employee)

    def get_all_pilots(self):
        return self.data_wrapper.get_all_pilots()
    
    def get_all_cabincrews(self):
        return self.data_wrapper.get_all_cabincrews()
