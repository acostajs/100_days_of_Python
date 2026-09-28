# This are the helper functions for the task of Day 10 of 100 days of Python


def calc(operator: str, first_number: float, second_number: float):
    """
    Calculates the result.
    Args:
        Operator: Chooses which operation to make.
        first_number: The number on which the operation is made.
        second_number: The number to operates.

    Returns:
        The result of the operation between first_number and second_number.
    """
    try:
        match operator:
            case "+":
                return first_number + second_number
            case "-":
                return first_number - second_number
            case "*":
                return first_number * second_number
            case "/":
                return first_number / second_number
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero")
