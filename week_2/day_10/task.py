# This is the task for Day 10 of 100 days of Python

from common.common_art import COMMON_ART
from common.toolkit import clear_terminal
from common.validators import validate_float, validate_input
from .utils import calc
from .task_art import TASK_ART


def main():
    calculator = "on"
    previous_calc = "n"
    result = 0

    while calculator == "on":
        try:
            clear_terminal()
            print(TASK_ART["title"])
            print(COMMON_ART["divider"])
            if previous_calc == "y":
                first_number = result
                print(f"Previous result: {first_number}")
            else:
                first_number = validate_float("What's the first number:\n - ")

            operator = validate_input(
                '"+", "-", "*", "/"\n Pick an operation:\n - ', ["+", "-", "*", "/"]
            )
            second_number = validate_float("What's the second number:\n - ")
            result = calc(operator, first_number, second_number)
        except ValueError as error:
            print(f"Error: {error}. Please try again.\n")
            continue

        print(f"{first_number} {operator} {second_number} = {result}")
        print(COMMON_ART["divider"])
        continue_or_not = validate_input(
            "Type 'y' to continue, 'n' for new calculation, 'esc' to quit:\n - ",
            ["y", "n", "esc"],
        )
        print(COMMON_ART["divider"])

        if continue_or_not == "y":
            previous_calc = "y"
        elif continue_or_not == "n":
            previous_calc = "n"
        elif continue_or_not == "esc":
            calculator = "off"


if __name__ == "__main__":
    main()
