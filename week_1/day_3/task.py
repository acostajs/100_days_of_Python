# This is Day 3 of 100 days of Python

from common.common_art import COMMON_ART
from common.validators import validate_input
from common.toolkit import clear_terminal
from .task_art import TASK_ART
from .utils import check_step
from .data import STEPS


def main():

    play_again = "y"
    while play_again == "y":
        print(TASK_ART["title"])
        print("Welcome to Treasure Island.\nYour mission is to find the treasure")
        print(COMMON_ART["divider"])

        won = True
        for step in STEPS:
            if not check_step(
                step["prompt"],
                step["options"],
                step["correct_answer"],
                step["fail_message"],
            ):
                won = False
                break

        if won:
            print(TASK_ART["treasure"])
            print("You WIN! You have found the TREASURE!")

        print(COMMON_ART["divider"])
        play_again = validate_input(
            "Do you want to play again? Type 'y' or 'n':\n - ", ["y", "n"]
        )
        clear_terminal()


if __name__ == "__main__":
    main()
