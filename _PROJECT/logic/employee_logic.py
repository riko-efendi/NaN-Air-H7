class EmployeeLogic:
    def __init__(self, data_connection) -> None:
        self.data_wrapper = data_connection

    def get_all_employees(self):
        return self.data_wrapper.get_all_employees()
    
    def register_employee(self, employee):
        return self.data_wrapper.register_employee(employee)
    
    def view_employee(self, kennitala):
        for employee in self.data_wrapper.get_all_employees():
            if kennitala == employee.kennitala:
                return employee.name

    def get_all_pilots(self):
        return self.data_wrapper.get_all_pilots()
    
    def get_all_cabincrews(self):
        return self.data_wrapper.get_all_cabincrews()
