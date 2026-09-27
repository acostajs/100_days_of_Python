# This runs the menu for each task(script) done for week 1 of 100 Days of Python

from common.data import week_1
from common.toolkit import clear_terminal, menu


def main():
    menu("day_", week_1, "back", "task", __package__, True)
    clear_terminal()
