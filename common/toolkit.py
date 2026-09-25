# This is the common tools used during 100 days of Python

import importlib
import sys
from pathlib import Path


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
