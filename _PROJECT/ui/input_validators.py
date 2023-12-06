class NameLengthException(Exception):
    pass


def validate_name(name):
    if len(name) >= 50:
        raise NameLengthException()
    if not name.isalpha():
        raise ValueError("Name must only contain letters")
    else:
        return True
    

def validate_kennitala(kennitala):
    if len(kennitala) != 10: 
        raise ValueError("This kennitala is either too long or too short")
    if not kennitala.isdigit():
        raise ValueError("The kennitala must only contain digits")
    else: 
        return True
        
    
def validate_phone_number(phone_number):
    if len(phone_number) < 8 or len(phone_number) > 12:
        raise ValueError("This phone number is either too long or too short")
    if not phone_number.isdigit():
        raise ValueError("The phone Number must only contain digits")
    else:
        return True
    
