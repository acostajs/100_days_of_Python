# This is Day 12 of 100 days of Python

import random
import os

from helpers import *
from ascii_art import ascii_art

def main():

    while True:
        print(ascii_art("title"))
        print("Welcome to the Number Guessing Game!")
        difficulty = validate_input("Choose a difficulty. Type 'easy', 'medium', or 'hard':\n - ", {"easy", "medium", "hard"})
        range = ""
        if difficulty == "easy":
            range = "1 and 10"
        elif difficulty == "medium":
            range = "1 and 100"
        elif difficulty == "hard":
            range = "1 and 1000"
        print(f"Im thinking of a number between {range}")
        number = random_number(difficulty)
        attempts = number_of_attempts(difficulty)
        check_guess(number, attempts)
        
        play_another = validate_input("Do you want to play again? Type 'y' or 'n':\n - ", { "y", "n"})
        os.system('cls' if os.name == 'nt' else 'clear')
        if play_another == 'n':
            break


if __name__ ==  "__main__":
    main()
