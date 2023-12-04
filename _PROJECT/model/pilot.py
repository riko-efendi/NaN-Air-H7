from employee import Employee

class Pilot(Employee):
    def __init__(self, rank="Co-Pilot"):
        super().__init__()
        self.rank = rank