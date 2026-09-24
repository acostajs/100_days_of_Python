# This is the main menu for the whole 100 days of Python

from common.ascii_art import ascii_art
from common.validators import validate_input
from common.toolkit import print_menu
from pathlib import Path


def weeks() -> list[str]:
    weeks = []
    for item in Path(".").iterdir():
        if item.is_dir() and item.name.startswith("week_"):
            weeks.append(item.name)

    return weeks

def main():
    
    options = {
        "week_1" : "Python Fundamentals",
        "week_2" : "Functions, Data Structures & Debugging",
        "week_3" : "OOP & Turtle Graphics",
        "week_4" : "Gaames, Files & Pandas Intro",
        "week_5" : "GUI Apps & APIs",
        "week_6" : "APIs, Capstones & Web Foundations",
        "week_7" : "CSS & Web Scraping",
        "week_8" : "Automation Bots & Flask Intro",
        "week_9" : "Flask Templating, Forms & Databases",
        "week_10" : "Web Design, REST APIs & Auth",
        "week_11" : "Deployment & Data Analysis",
        "week_12" : "Statistics & Data Science Capstone",
        "week_13" : "Portfolio Projects 1",
        "week_14" : "Portfolio Projects 2",
        "week_15" : "Final Projects & Wrap-up"
    }
           
    choices = weeks()
    print(ascii_art("menu"))
    print(ascii_art("divider"))
    while True:
        print("Choose one of the following weeks to check their corresponding tasks:")
        print_menu(options, choices)
        user_choice = validate_input("Type 'week_' plus the number of the week: e.g. 'week-1'\n - ", choices)
        
    
if __name__ == "__main__":
    main()
