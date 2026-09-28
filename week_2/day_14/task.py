# This is day 14 of 100 days of Python

from common.common_art import COMMON_ART
from .task_art import TASK_ART
from common.validators import validate_input
from common.toolkit import clear_terminal
from .utils import random_celebrities, format_choice, check_answer
from .data import CELEBRITIES


def main():

    attempts = 1
    score = 0
    play = "y"
    while play == "y":
        while attempts == 1:
            choice_a, choice_b = random_celebrities(CELEBRITIES)
            print(TASK_ART["title"])
            print(COMMON_ART["divider"])

            if score > 0:
                print(f"You're RIGHT! Your current score: {score}")

            print(f"Compare A: {format_choice(choice_a)}")
            print(TASK_ART["vs"])
            print(f"Against B: {format_choice(choice_b)}")

            user_choice = validate_input(
                "Who has more followers? Type 'A' or 'B': - ", ["a", "b"]
            )
            answer = check_answer(user_choice, choice_a, choice_b)
            if answer == True:
                score += 1
            else:
                attempts -= 1

        clear_terminal()

        print(TASK_ART["title"])
        print(COMMON_ART["divider"])
        print(f"Sorry, that's wrong. Final score: {score}")
        play = validate_input("Want to play again? Type 'y' or 'n':\n - ", ["y", "n"])
        if play == "y":
            attempts = 1
            score = 0


if __name__ == "__main__":
    main()
