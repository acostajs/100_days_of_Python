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

