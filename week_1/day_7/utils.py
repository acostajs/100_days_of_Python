import random
from .data import WORDS, INSTRUCTIONS


def random_word() -> str:
    """
    This function returns a random word from a list of words.
    """

    random_word = random.choice(WORDS)
    return random_word


def print_intro():
    print(INSTRUCTIONS["intro"])
    for step in INSTRUCTIONS["instructions"]:
        print(step)
