# This module returns a random word from a list
import random


def random_word() -> str:
    """
        This function returns a random word from a list of words.
    """
    words = [
        "python",
        "keyboard",
        "elephant",
        "guitar",
        "mountain",
        "sandwich",
        "umbrella",
        "penguin",
        "volcano",
        "bicycle",
        "dinosaur",
        "chocolate",
        "telescope",
        "backpack",
        "dolphin",
        "rainbow",
        "castle",
        "spaceship",
        "butterfly",
        "wizard",
    ]

    random_word = random.choice(words)
    return random_word
