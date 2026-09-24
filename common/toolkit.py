# This is the common tools used during 100 days of Python

def print_menu(options: dict, choices: list):
   
    for key, value in options.items():
        if key in choices:
            print(f"{key} : {value}")

