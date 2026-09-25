# This runs the menu for each task(script) done for week 1 of 100 Days of Python


from common.toolkit import print_menu, modules, run_module, clear_terminal
from common.ascii_art import ascii_art
from common.validators import validate_input

def main():
    tasks = {
        "day_1": "Working with variables in Python to manage data.",
        "day_2": "Understanding data types and how to manipulate strings.",
        "day_3": "Control flow and logical operators.",
        "day_4": "Randomisation and Python lists.",
        "day_5": "Python loops.",
        "day_6": "Python functions and Karel.",
        "day_7": "Hangman"
    }
 
    while True:
        choices = modules("day_", True)
        choices.append("back")
        print(ascii_art("menu"))
        print(ascii_art("divider"))
        print("Choose one of the corresponding tasks to run the script:")
        print_menu(tasks, choices)
        
        user_choice = validate_input("Type 'day_(number) to choose a day'\nType 'back' to go to the main menu\n - ", choices)
        if user_choice == "back":
            break
        else:
            clear_terminal()
            run_module(user_choice, "task", __package__)
            clear_terminal()

if __name__ == "__name__":
    main()
