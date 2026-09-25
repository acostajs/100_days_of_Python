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

def format_choice(data: dict) -> str:
    return f"{data["name"]}, {data["known_for"]}, from {data["origin"]}"

def check_answer(user_answer: str, choice_a: dict, choice_b: dict) -> bool:
    if choice_a["followers"] > choice_b["followers"]:
        return user_answer == "a"
    else:
        return user_answer == "b"
