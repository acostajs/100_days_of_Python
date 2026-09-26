# This is Day 2 of 100 days of Python

from common.common_art import COMMON_ART
from common.validators import validate_float, validate_int, validate_input
from .task_art import TASK_ART
from .utils import calculate_total_bill, calculate_tip


def main():
    print(TASK_ART("title"))
    print(COMMON_ART("divider"))

    name = input("Hi! what is your name? : ")

    while True:
        print(f"Hi! {name}, let's calculate how much you have to pay for the tip\nAnswer the following questions")
        bill = validate_float("What was the bill? $")
        tip_percentage = validate_float("How much tip would you like to give? 10, 15, maybe 20? %")
        people = validate_int("How many people to split the bill with? ")
        tip = calculate_tip(bill, tip_percentage, people)
        total_bill = calculate_total_bill(bill, tip_percentage, people)
        print(f"{name}, the tip is ${tip} and your total bill to pay is ${total_bill}")

        play_again = validate_input("Want to calculate another tip?:\n - ", ['y', 'n'])
        if play_again == 'n':
            break

    print(COMMON_ART["goodbye"])
    print(COMMON_ART["divider"])
if __name__ == "__main__":
    main()
 
