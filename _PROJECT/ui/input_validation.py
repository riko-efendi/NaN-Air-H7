class LengthERROR(Exception):
    pass

class DateError(Exception):
    pass


###############################################################################################################
#[EMPLOYEE MENU]#
    
def validate_name(name):
    if name.isalpha() == False:
        raise ValueError
    if (0 < len(name) <= 20) == False:
        raise LengthERROR
    #validates the length of the name and if the name only contains letters 

def validate_kennitala(kennitala): #needs to create a new one and cannot create an existing one. 
    if kennitala.isdigit() == False:
        raise ValueError
    if len(kennitala) != 10 and len(kennitala) != 9:
        raise LengthERROR
    #this validates the kennitala length i saw that there were some that were 10 and some that were 9


def validate_phone_number(phone_number):
    if phone_number.isdigit() == False:
        raise ValueError
    if len(phone_number) != 7:
        raise LengthERROR
    #this checks the length of the phone number

def validate_address(address):
    address_list = address.split()
    if len(address_list) != 2:
        raise LengthERROR
    first, second=address_list
    if first.isdigit() or second.isalpha():
        raise ValueError
    if not (1 <= len(first) <= 25 and 1 <= len(second) <= 2):
        raise LengthERROR
    #this is an example of mixing things together
    #this validates that the address is valid.


def validate_input_view_by_kt(user_input):
    valid_input = ("w","u","k","b")
    if user_input.lower() not in valid_input:
        raise ValueError
    #this was used for the list employee via kennitala. 

def validate_year_format(date):
    date_list = date.split("-")
    for element in date_list:
        if element.isdigit == False:
            raise ValueError
    if len(date_list) != 3:
        raise LengthERROR
    elif len(date_list[0]) != 4 or len(date_list[1]) != 2 or len(date_list[2]) != 2:
        raise LengthERROR
    elif int(date_list[1]) > 12 or int(date_list[2]) > 31:
        raise DateError


###############################################################################################################
#[VOYAGE MENU]#

#register_destinations.

def validate_id(id):
    if id.isalpha() == False:
        raise ValueError
    if len(id) != 3:
        raise LengthERROR
    
def validate_name_destination(destination):
    if destination.isalpha() == False:
        raise ValueError
    if (0 < len(destination) <= 25) == False:
        raise LengthERROR

def validate_numeric_id(numeric_id):
    if numeric_id.isdigit() == False:
        raise ValueError
    if len(numeric_id) != 4:
        raise LengthERROR
    
def validate_flight_time(flight_time):
    if flight_time.isdigit() == False:
        raise ValueError
    if (0 < int(flight_time) <= 20) == False:
        raise LengthERROR