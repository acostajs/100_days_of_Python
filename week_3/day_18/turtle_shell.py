from turtle import Turtle, Screen
from random import choice, randint
from common.validators import validate_input, validate_int
from .data import COLORS, SHAPES


class TurtleShell:
    def __init__(self):
        self.screen = Screen()
        self.turtle = Turtle()
        self.menu = {
            "move": {
                "forward": (self.turtle.forward, "int"),
                "backward": (self.turtle.backward, "int"),
                "turn left": (self.turtle.left, "int"),
                "turn right": (self.turtle.right, "int"),
            },
            "pen": {
                "up": (self.turtle.penup, None),
                "down": (self.turtle.pendown, None),
                "color": (self.turtle.pencolor, "color"),
                "size": (self.turtle.pensize, "int"),
            },
            "turtle": {
                "color": (self.turtle.fillcolor, "color"),
                "shape": (self.turtle.shape, "shape"),
                "reset": (self.turtle.reset, None),
            },
            "canvas": {
                "background color": (self.screen.bgcolor, "color"),
            },
            "draw": {
                "square": (self.draw_square, None),
                "dashed line": (self.draw_dashed_line, None),
                "dot": (self.turtle.dot, "int"),
                "circle": (self.turtle.circle, "int"),
                "spirograph": (self.draw_spirograph, None),
                "dot wall": (self.draw_dot_wall, None),
                "random walk": (self.draw_random_walk, None),
            },
        }

    def random_color(self, colors):
        return choice(colors)

    def ask_argument(self, kind):
        """Return the arguments to pass, based on the kind of input needed."""
        if kind == "int":
            return (validate_int("by how much? "),)
        if kind == "color":
            return (validate_input(f"{COLORS}\n - ", COLORS),)
        if kind == "shape":
            return (validate_input(f"{SHAPES}\n - ", SHAPES),)
        return ()

    def draw_square(self):
        side_length = validate_int("Input the length of the side of the square:\n - ")
        turn = 90
        for _ in range(4):
            self.turtle.forward(side_length)
            self.turtle.left(turn)

    def pen_is_down(self):
        was_down = self.turtle.isdown()
        if was_down:
            self.turtle.pendown()

    def draw_dashed_line(self):
        self.pen_is_down()
        length = validate_int("Input the length of the dashed line:\n - ")
        drawn_length = 0
        while drawn_length < length:
            self.turtle.forward(4)
            self.turtle.penup()
            self.turtle.forward(4)
            self.turtle.pendown()
            drawn_length += 8

    def draw_spirograph(self):
        radius = validate_int("Choose the radius:\n - ")
        spacing = validate_int("Choose the spacing:\n - ")
        quantity = validate_int("Choose how many repetitions:\n - ")
        repeats = 0
        while repeats < quantity:
            self.turtle.circle(radius)
            self.turtle.left(spacing)
            repeats += 1

    def draw_dot_wall(self):
        dot_size = validate_int("Choose the size of the dot:\n - ")
        spacing = validate_int("Choose the spacing between dots:\n - ")
        total_lines = validate_int("Choose the total lines of dots to draw:\n - ")
        dots_per_line = validate_int("How mamy dots per line:\n - ")
        start_x = -200
        start_y = 0

        self.turtle.penup()
        self.turtle.setheading(0)

        for line in range(total_lines):
            self.turtle.goto(start_x, start_y + line * spacing)
            for _ in range(dots_per_line):
                self.turtle.dot(dot_size, choice(COLORS))
                self.turtle.forward(spacing)

    def draw_random_walk(self):
        random_range = randint(0, 200)
        turn = [90, 270]
        self.pen_is_down()
        for _ in range(random_range):
            self.turtle.pencolor(choice(COLORS))
            self.turtle.pensize(randint(4, 10))
            self.turtle.forward(randint(0, 100))
            left_or_right = randint(0, 1)
            if left_or_right == 1:
                self.turtle.left(choice(turn))
            else:
                self.turtle.right(choice(turn))

    def run(self):

        menu = list(self.menu)
        menu += ["quit"]

        while True:
            user_choice = validate_input(
                f"{menu} Choose what to do:\n - ",
                menu,
            )
            if user_choice == "quit":
                self.screen.bye()
                break

            actions = self.menu[user_choice]
            list_of_actions = list(actions) + ["back"]
            user_choice = validate_input(
                f"{list_of_actions}\n Choose an action:\n - ", list_of_actions
            )
            if user_choice == "back":
                continue

            action, kind = actions[user_choice]
            action(*self.ask_argument(kind))
