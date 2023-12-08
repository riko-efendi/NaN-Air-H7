# Here I am trying to build a functionality within the software that would allow the user to see which employee was working on what flight
# at what particular time of the week. 



class Schedule:
    def __init__(self, file_name= "_PROJECT/files/past_flights.csv", file_name_2 = "_PROJECT/files/crew.csv") -> None:
        self.file_name = file_name
        self.read_file(file_name="_PROJECT/files/past_flights.csv")
        self.file_name_2 = file_name_2
        self.get_schedule()
        self.employees = []
        self.get_employee_names(file_name_2= "_PROJECT/files/crew.csv")


    def read_file(self, file_name: str):
        with open(file_name, "r") as data_file:
            data = data_file.readlines()
            return data

    def get_schedule(self):
        day = str(input())
        for line in self.read_file(file_name):
            row = line.strip().split(',')
            # Assuming row[3] contains the employee information
            employee_info = row[3]
            if employee_info == "2023-11-" + day: 
                self.employees.append(row)
                return self.employees
            

    def get_employee_names(self,file_name_2):
        print("Hæ")
        crew = []
        right_employees = []
        with open (file_name_2, "r") as data_file: 
            data = data_file.readlines()
            for line in data:
                row = line.strip().split(',')
            crew.append(row)
        if self.employees[6] == crew[0]:
            right_employees.append(crew)
            print("Hæ")
        elif self.employees[7] == crew[0]:
            right_employees.append(crew)
            print("Hæ")
        elif self.employees[8] == crew[0]:
            right_employees.append(crew)
            print("Hæ")
        elif self.employees[9] == crew[0]:
            right_employees.append(crew)
            print("Hæ")
        elif self.employees[10] == crew[0]:
            right_employees.append(crew)
            print("Hæ")
        print(right_employees)
        
            
        

        

            
            

            
            # Print the employee_info for each line
       

# Example usage
file_name = "_PROJECT/files/past_flights.csv"
schedule_instance = Schedule(file_name)
