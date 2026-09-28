# This is day 1 of 100 days of Python

from .task_art import TASK_ART
from common.validators import validate_int, validate_input
from common.common_art import COMMON_ART


def main():

    print(TASK_ART["title"])
    name = input("Hi! what is your name? : ")
    while True:
        name_length = len(name)
        print(
            f"{name}, this is your band name generator\nLet's start with a couple of questions."
        )
        city = input("1. What city were you born in? : ")
        pet = input("2. What was the name of your first pet? : ")
        number = validate_int("3. Choose a number between 1 and 10: ")
        band_number = name_length * number
        print(f"{name}, your band name is {city} {pet} {band_number}")

        play_again = validate_input(
            "Do you want to play again? Type 'y' or 'n':\n - ", ["y", "n"]
        )
        print(COMMON_ART["divider"])

        if play_again == "n":
            break

    print(COMMON_ART["divider"])


if __name__ == "__main__":
    main()
