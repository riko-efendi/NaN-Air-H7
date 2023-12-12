
class LengthERROR(Exception):
    pass





def validate_length(name):
    if 0 < len(name) <= 20:
        pass
    else:
        raise LengthERROR
    #validates the length of the name 
def validate_length_kt(kennitala):
    if len(kennitala) != 10 and len(kennitala) != 9:
        raise LengthERROR
    #this validates the kennitala length i saw that there were some that were 10 and some that were 9
def validate_letters(name):
    if name.isalpha() == False:
         raise ValueError
    #this checks if the input was just letters
def validate_integers(number):
    if number.isdigit() == False:
        raise ValueError
    #this individuall checks if what the user inputed was a number

    ### i might mix these later with the others to clean it out better.


def validate_length_phone(phone_number):
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