# This runs the menu for each task(script) done for week 2 of 100 Days of Python

from common.data import week_2
from common.toolkit import menu, clear_terminal


def main():
    menu("day_", week_2, "back", "task", __package__, True)
    clear_terminal()
