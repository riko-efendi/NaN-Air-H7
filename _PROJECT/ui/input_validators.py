class InputError(Exception):
    pass

def validate_letters(name):
    if name.isalpha() == False:
         raise InputError

def validate_integers(number):
    if number.isdigit() == False:
        raise InputError
    
def validate_address(address):
    address_list = address.split()
    if len(address_list) != 2:
        raise InputError
    elif address_list[0].isalpha() == False:
        raise InputError
    elif address_list[1].isdigit() == False:
        raise InputError