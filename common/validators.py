# This module contains all the custom validators used throughout different tasks in 100 days of Python

def validate_input(prompt: str, choices: list) -> str:
    """
        Validate that the user only inputs one of the posible choices.
        Receives prompt message to display, and a set of possible choices.
        Returns a valid choice.
    """
    valid_choices = choices
    choice = input(prompt).lower()
    while choice not in valid_choices:
        choice = input(f"Wrong input: Type {valid_choices}:\n - ").lower()

    return choice

def validate_int(prompt: str) -> int:
    """
        Validates that the user only writes integers in their answer.
        Receives prompt message to display.
        Returns the integer.
    """
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print("Wrong Input: Please enter a valid integer")

def validate_float(prompt: str) -> int:
    """
        Validates that the user only writes integers in their answer.
    """
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Wrong Input: Please enter a valid float")
