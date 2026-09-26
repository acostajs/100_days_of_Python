# This is the main menu for the whole 100 days of Python

from common.common_art import COMMON_ART
from common.validators import validate_input
from common.toolkit import print_menu, modules, run_module, clear_terminal
from common.data import main_menu


def main():

    while True:
        choices = modules("week_")
        choices.append("esc")
        print(COMMON_ART["menu"])
        print(COMMON_ART["divider"])
        print("Choose one of the following weeks to check their corresponding tasks:")
        print_menu(main_menu, choices)

        user_choice = validate_input(
            "Type 'week_(number)' to choose a week\nType 'esc' to quit\n - ", choices
        )
        if user_choice == "esc":
            break
        else:
            clear_terminal()
            run_module(user_choice)
            clear_terminal()

    print(COMMON_ART["goodbye"])


if __name__ == "__main__":
    main()
