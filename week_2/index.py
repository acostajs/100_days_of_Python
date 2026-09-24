# This runs the menu for each task(script) done for week 2 of 100 Days of Python

from common.toolkit import print_menu, modules, run_module, clear_terminal
from common.ascii_art import ascii_art
from common.validators import validate_input

def main():
    tasks = {
        "day_8": "Function Parameters and Caesar Cipher.",
        "day_9": "Dictionaries, Nesting and the Secret Auction.",
        "day_10": "Functions with outputs.",
        "day_11": "The blackjack capstone project.",
        "day_12": "Scope and Number guessing game.",
        "day_13": "Debugging: How to find and fix errors in your code.",
        "day_14": "Higher Lower Game Project."
    }

    

    while True:
        choices = modules("day_", True)
        print(ascii_art("menu"))
        print(ascii_art("divider"))
        print("Choose one of the corresponding tasks to run the script:")
        print_menu(tasks, choices)
        user_choice = validate_input("Type 'day_' plus the number of the day to run the task. e.g. 'day_1', 'day_6'\n - ", choices)
        clear_terminal()
        run_module(user_choice, "task", __package__)
        print(ascii_art("divider"))
        print(ascii_art("menu"))
        print(ascii_art("divider"))
        user_choice = validate_input("Type 'back' to go back to main menu, type 'continue' to keep running tasks from this week\n - ", ['back', 'continue'])
        clear_terminal()
        if user_choice == 'back':
            break

        
    

if __name__ == "__name__":
    main()

