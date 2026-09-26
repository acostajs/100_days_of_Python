# This is the common tools used during 100 days of Python

import importlib
import sys
from pathlib import Path
from common.common_art import COMMON_ART
from common.validators import validate_input


def print_menu(options: dict, choices: list):

    for key, value in options.items():
        if key in choices:
            print(f"{key} : {value}")


def modules(folder_start: str, recursive: bool = False) -> list[str]:
    """
    Receives the initial part of the name of the list of folders. e.g "week_", "day_"
    It loops to find all the folders that start with folder_start.
    Returns a list of all the folders found.
    """
    base_dir = Path(__file__).resolve().parent.parent

    items = base_dir.rglob("*") if recursive else base_dir.iterdir()
    folders = []

    for item in items:
        if item.is_dir() and item.name.startswith(folder_start):
            folders.append(item.name)

    folders.sort()
    return folders


def run_module(
    module_name: str,
    file_name: str = "index",
    parent_package: str | None = None,
) -> None:
    if parent_package:
        full_name = f"{parent_package}.{module_name}.{file_name}"
    else:
        full_name = f"{module_name}.{file_name}"

    imported_module = importlib.import_module(full_name)
    imported_module.main()


def clear_terminal() -> None:
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()


def weekly_menu(data: dict, package: str):

    while True:
        choices = modules("day_", True)
        choices.append("back")
        print(COMMON_ART["menu"])
        print(COMMON_ART["divider"])
        print("Choose one of the corresponding tasks to run the script:")
        print_menu(data, choices)

        user_choice = validate_input(
            "Type 'day_(number) to choose a day'\nType 'back' to go to the main menu\n - ",
            choices,
        )
        if user_choice == "back":
            break
        else:
            clear_terminal()
            run_module(user_choice, "task", package)
