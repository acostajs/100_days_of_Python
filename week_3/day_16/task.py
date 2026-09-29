# Day 16 of 100 days of Python
import turtle
from turtle import Turtle, Screen
from common.validators import validate_input, validate_int


def main():
    turtle.TurtleScreen._RUNNING = True

    timmy = Turtle()
    timmy.shape("turtle")

    actions = {
        "forward": timmy.forward,
        "backward": timmy.backward,
        "left": timmy.left,
        "right": timmy.right,
    }

    while True:
        user_choice = validate_input(
            "What do you want to do? move 'forward/backward', turn 'left/right', or 'esc' to finish\n - ",
            [*actions, "esc"],
        )

        if user_choice == "esc":
            break

        steps = validate_int("how much?\n - ")
        actions[user_choice](steps)

    Screen().bye()
