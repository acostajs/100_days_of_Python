# This is the main menu for the whole 100 days of Python

from common.common_art import COMMON_ART
from common.data import main_menu
from common.toolkit import menu, clear_terminal


def main():
    try:
        clear_terminal()
        menu("week_", main_menu, "exit", "index", recursive=False)
        clear_terminal()
        print(COMMON_ART["goodbye"])
    except KeyboardInterrupt:
        print("\nProgram Interrupted. Exiting gracefully.")


if __name__ == "__main__":
    main()
