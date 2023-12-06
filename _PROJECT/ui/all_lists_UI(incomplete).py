# Here is the Class Lists. 
# The only thing this class should be able to do is print out lists.
# It should be able to read all csv data files and print out from them accordingly.
# if in any menu the user chooses to list something (e. employees, voyages etc.) this class should get to work


class List:
    def __init__(self, file_name: str) -> None:
        self.data_file = self.read_file(file_name)
        self.print_file(self.data_file)

    def read_file(self, file_name: str):
        with open(file_name, "r") as data_file:
            data = data_file.readlines()
            return data
    # Here the function reads the appropriate file 

    def print_file(self, data):
        print(data)


    # And Here the function prints out the file already read by read_file()


    # TODO
    # How can I incorporate this class?
    # How can the user exit this list?
    # Can he return back from whence he came?
    

    # TODO 2
    # How can I format the List
    # the List should be formatted with the prettytable module. 
    
