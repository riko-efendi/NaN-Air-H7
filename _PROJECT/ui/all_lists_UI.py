# Here is the Class Lists. 
# The only thing this class should be able to do is print out lists.
# It should be able to read all csv data files and print out from them accordingly.
# if in any menu the user chooses to list something (e. employees, voyages etc.) this class should get to work

# from model.voyage import Voyage
from prettytable import PrettyTable
from typing import List as TypingList

class TextColors:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"

class List:
    def __init__(self, file_name: str) -> None:
        self.data_file = self.read_file(file_name)
        self.print_file(self.data_file)

    def read_file(self, file_name: str):
        with open(file_name, "r") as data_file:
            data = data_file.readlines()
            return data

    def print_file(self, data):
        table = PrettyTable()
        delimiter = ','
        header = data[0].strip().split(delimiter)
        table.field_names = header

        for idx, row in enumerate(data[1:], start=1):
            row_data = row.strip().split(delimiter)
            if len(row_data) != len(header):
                print(f"Warning at row {idx}: {row_data}. Skipping this row.")
                continue
            table.add_row(row_data)

        table_string = table.get_string()
        print(table_string)

# Example usage
file_name = "_PROJECT/files/crew.csv"
list_instance = List(file_name)



    # And Here the function prints out the file already read by read_file()




    # TODO
    # How can I incorporate this class?
    # How can the user exit this list?
    # Can he return back from whence he came?
    

    # TODO 2
    # How can I format the List
    # the List should be formatted with the prettytable module. 

# print(TextColors.GREEN + "This text is green." + TextColors.RESET)