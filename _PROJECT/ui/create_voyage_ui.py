class CreateVoyageUI():
    def __init__(self, wrapper) -> None:
        self.logic_wrapper = wrapper

    def create_voyage(self, voyage):
        """Creates a voyage"""

        print("\n[CREATE VOYAGE]\n")
        voyage.flight_out = input("Input the flight out: ")
        voyage.flight_in = input("Input the flight in: ")

        pilot = input("Input the pilot: ")
        cabincrew = input("Input the cabin crew: ")
        if pilot != None: 
            pass
        if cabincrew != None:
            pass

        #Add crew(optional?)
        self.logic_wrapper.create_voyage(voyage)
        print(f"\n{voyage.flight_out}-{voyage.flight_in} is successfully created.")
