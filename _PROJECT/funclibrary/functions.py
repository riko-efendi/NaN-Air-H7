import os

def clear_screen():
    os_name = os.name.lower()

    if os_name == 'posix':  # Unix/Linux/MacOS
        os.system("clear")
    elif os_name == 'nt':   # Windows
        os.system("cls")
