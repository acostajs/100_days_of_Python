# util functions to help with the task for Day 14 of 100 days of Python

from random import choice


def random_celebrities(celebrities: list[dict]) -> tuple[dict, dict]:
    """
        Receives a list of dictionaries,
        Returns a tuple of random dictionaries.
    """
    choice_a = choice(celebrities)
    choice_b = choice(celebrities)
    while choice_b == choice_a:
        choice_b = choice(celebrities)
    
    return choice_a, choice_b

