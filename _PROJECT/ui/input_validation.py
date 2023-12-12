class LengthERROR(Exception):
    pass

def validate_length(name):
    if 0 < len(name) <= 20:
        pass
    else:
        raise LengthERROR()
    
def validate_length_kt(kennitala):
    if len(kennitala) > 10:
        raise LengthERROR()

def validate_letters(name):
    if name.isalpha() == False:
         raise ValueError()

def validate_integers(number):
    if number.isdigit() == False:
        raise ValueError()

def validate_length_phone(phone_number):
    if len(phone_number) != 7:
        raise LengthERROR()
    
def validate_address(address):
    address_list = address.split()
    if len(address_list) != 2:
        raise ValueError()
    elif address_list[0].isalpha() == False:
        raise ValueError()
    elif address_list[1].isdigit() == False:
        raise ValueError()  