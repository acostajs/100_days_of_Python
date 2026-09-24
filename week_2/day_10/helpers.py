# This are the helper functions for the task of Day 10 of 100 days of Python


def calc(operator, first_number, second_number):
    """
        Calculates the result.
        Args:
            Operator: Chooses which operation to make.
            first_number: The number on which the operation is made.
            second_number: The number to operates.

        Returns:
            The result of the operation between first_number and second_number.
    """
    if operator == "/" and second_number == 0:
        raise ValueError("Cannot divide by zero")
    
    match operator:
        case "+":
            return first_number + second_number
        case "-":
            return first_number - second_number
        case "*":
            return first_number * second_number
        case "/":
            return first_number / second_number

def continue_calc(message: str, wrong_message: str) -> bool:
    """
        From the user input it determines whether to continue or not calculating.

        Args:
            message: prompt to display to the user.
            wrong_message: prompt display to the user for wrong input.

        Returns:
            The validation of the user choice.
    """
    user_choice = input(f"{message}")
    while user_choice != True or user_choice != False:
        if user_choice == 'y':
            user_choice = True
        elif user_choice == 'n':
            user_choice = False
        else:
            user_choice = input(f"{wrong_message}")

    return bool(user_choice)

def validate_int(prompt: str) -> int:
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print("Wrong Input: Please enter a valid integer")

def validate_choice(valid_inputs: set, user_input: str) -> str:
    valid_choices = valid_inputs
    choice = user_input
    while choice not in valid_choices:
        choice = input(f"Wrong Input: type {valid_choices}\n - ")

    return choice
