# This is Day 5 of 100 days of Python

from .task_art import TASK_ART
from common.common_art import COMMON_ART
from common.validators import validate_input
from common.toolkit import clear_terminal
from .utils import password_generator


def main():

    play = "y"
    while play == "y":
        print(TASK_ART["title"])
        print("Welcome to the Password Generator")
        print(COMMON_ART["divider"])
        amount_letters = int(
            input("How many letters would you like in your password?:\n - ")
        )
        amount_digits = int(input("How many numbers would you like?:\n - "))
        amount_symbols = int(input("How many symbols would you like?:\n - "))

        password = password_generator(amount_letters, amount_digits, amount_symbols)

        print(f"Your password is: {password}")
        play = validate_input(
            "Do you want to generate a new password? Type 'y' or 'n':\n - ", ["y", "n"]
        )
        clear_terminal()


if __name__ == "__main__":
    main()
