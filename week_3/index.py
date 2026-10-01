# This runs the menu for each task(script) done for week 3 of 100 Days of Python

from common.data import week_3
from common.toolkit import menu, clear_terminal


def main():
    clear_terminal()
    menu("day_", week_3, "back", "task", __package__, True)
    clear_terminal()
