from datetime import datetime, date

class LengthError(Exception):
    pass

class DateRangeError(Exception):
    pass



def validate_length(name):
    if 0 < len(name) <= 20:
        pass
    else:
        raise LengthError()
    
def validate_length_kt(kennitala):
    if len(kennitala) > 10:
        raise LengthError()

def validate_letters(name):
    if name.isalpha() == False:
         raise ValueError()

def validate_integers(number):
    if number.isdigit() == False:
        raise ValueError()

def validate_length_phone(phone_number):
    if len(phone_number) != 7:
        raise LengthError()
    
def validate_address(address):
    address_list = address.split()
    if len(address_list) != 2:
        raise ValueError()
    elif address_list[0].isalpha() == False:
        raise ValueError()
    elif address_list[1].isdigit() == False:
        raise ValueError()  
    
def validate_date_format(date):
    datetime.strptime(date, '%Y-%m-%d')
    
def validate_time_format(time):
    datetime.strptime(time, '%H:%M:%S')



def validate_date_range(start_date, end_date, start_time="00:00:00", end_time="00:00:00"):
    try:
        start_datetime = datetime.strptime(f"{start_date} {start_time}", '%Y-%m-%d %H:%M:%S')
        end_datetime = datetime.strptime(f"{end_date} {end_time}", '%Y-%m-%d %H:%M:%S')


        if end_datetime < start_datetime:
            raise DateRangeError

    except ValueError:
        raise ValueError
