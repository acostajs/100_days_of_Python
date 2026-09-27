# This is day 4 of 100 days of Python
import random
from .task_art import TASK_ART
from .utils import compare_choices
from common.common_art import COMMON_ART
from common.validators import validate_input
from common.toolkit import clear_terminal


def main():

    play = "y"
    while play == "y":
        choices = ["rock", "paper", "scissors"]

        print(TASK_ART["title"])
        print(COMMON_ART["divider"])

        user_choice = validate_input(
            "Choose between rock, paper or scissors: - ", choices
        )

        computer_choice = random.choice(choices)
        print(f"You've choosen {user_choice}")
        print(TASK_ART[user_choice])
        print(f"The computer choose {computer_choice}")
        print(TASK_ART[computer_choice])
        print(compare_choices(user_choice, computer_choice))

        play = validate_input("Want to play again? Type 'y' or 'n':\n - ", ["y", "n"])
        clear_terminal()


if __name__ == "__main__":
    main()
