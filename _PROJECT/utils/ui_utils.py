from model.employee import Employee
from model.voyage import Voyage
from logic.logic_wrapper import LogicWrapper
import os
import shutil

class UIUtils:
    
    def __init__(self) -> None:
        self.logic_wrapper = LogicWrapper()

    def clear_screen(self):
        os_name = os.name.lower()
        if os_name == 'posix':  # Unix/Linux/MacOS
            os.system("clear")
        elif os_name == 'nt':   # Windows
            os.system("cls")

    def print_employee(self, employee:Employee, header:str=""):
        """Prints out a table of information on an Employee"""

        self.clear_screen()
        print(header + "\n")
        print(f"Name: {employee.name}")
        print(f"Kt: {employee.kennitala}")
        print(f"Address: {employee.address}")
        print(f"Role: {employee.role}")
        print(f"Rank: {employee.rank}")
        print(f"Phone number: {employee.phone_number}")
        print()


    def print_voyages(self, voyages:Voyage, header:str=""):
        """Prints voyages and their crews"""
        self.clear_screen()
        print(f"{header}\n")


        for index, voyage in enumerate(voyages):
            captain = self.logic_wrapper.get_employee_by_nid(voyage.flight_1.captain)
            captain = captain.name if captain != None else "No Crew Assigned"
            copilot = self.logic_wrapper.get_employee_by_nid(voyage.flight_1.copilot)
            copilot = copilot.name if copilot != None else "No Crew Assigned"
            fsm = self.logic_wrapper.get_employee_by_nid(voyage.flight_1.fsm)
            fsm = fsm.name if fsm != None else "No Crew Assigned"
            fa1 = self.logic_wrapper.get_employee_by_nid(voyage.flight_1.fa1)
            fa1 = fa1.name if fa1 != None else "No Crew Assigned"
            fa2 = self.logic_wrapper.get_employee_by_nid(voyage.flight_1.fa2)
            fa2 = fa2.name if fa2 != None else "No Crew Assigned"

            print(f"{index + 1}. Voyage id:[{voyage.id}]")
            print(f"\tGoing a round trip from {voyage.flight_1.dep_from} to {voyage.flight_1.arr_at}.")
            print(f"\t[{voyage.depart_date}] - [{voyage.arr_date}]")
            print(f"\tCaptain:                {captain}")
            print(f"\tCopilot:                {copilot}")
            print(f"\tFlight Service Manager: {fsm}")
            print(f"\tFlight Attendant 1:     {fa1}")
            print(f"\tFlight Attendant 2:     {fa2}")
            print()


    def make_boarder(self, header_str = "blub"):

        header_str = "["+header_str+"]"
        
        terminal_size = shutil.get_terminal_size()
        width, height = terminal_size.columns, terminal_size.lines


        header_str_offset = 4
        header = "╔" + ("═"*header_str_offset) + header_str + "═" * (width - len(header_str) - 2 - header_str_offset) + "╗"
        footer = "╚" + "═" * (width - 2) + "╝"
        boarder = header + "\n"

        for _ in range(int((height - 2))-2):
            boarder += "║" + " " * (width - 2) + "║" + "\n"
        boarder += footer

        return boarder


    def append_string(self, backgrnd, overlay, x_offset=0, y_offset=0):
        backgrnd_list = backgrnd.split("\n")
        overlay_list = overlay.split("\n")

        # Calculate the center pivot

        x_offset = int(len(backgrnd_list[0]) / 2) - int(len(overlay_list[0]) / 2) + x_offset
        #y_offset = int(len(backgrnd_list) / 2) - int(len(overlay_list) / 2) + y_offset

        try:
            for i in range(y_offset, (y_offset + len(overlay_list))):
                backgrnd_list[i] = (
                    backgrnd_list[i][:x_offset] +
                    overlay_list[i - y_offset] +
                    backgrnd_list[i][x_offset + len(overlay_list[i - y_offset]) :]
                )
        except IndexError:
            return backgrnd

        result = "".join(element for element in backgrnd_list)
        return result