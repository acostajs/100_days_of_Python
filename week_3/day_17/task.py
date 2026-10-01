# Day 17 of 100 Days of Python
from common.validators import validate_input, validate_int
from common.toolkit import clear_terminal
from common.common_art import COMMON_ART
from .data import QUESTIONS
from .game import Game
from .user import User
from .task_art import TASK_ART


def main():
    user = User()
    game = Game(QUESTIONS)
    play = "y"
    while play == "y":
        clear_terminal()
        print(TASK_ART["title"])
        print(COMMON_ART["divider"])
        question_quantity = validate_int("How many questions do you want to play?\n - ")
        print(COMMON_ART["divider"])
        game.play(user, question_quantity)
        print(COMMON_ART["divider"])
        play = validate_input("Want to play again? Type 'y' or 'n'\n - ", ["y", "n"])
