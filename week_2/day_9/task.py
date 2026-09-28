# This is Day 9 of 100 days of Python


from .task_art import TASK_ART
from .utils import find_highest_bidder, loading_animation, bidding
from common.common_art import COMMON_ART
from common.toolkit import clear_terminal
from common.validators import validate_input, validate_int


def main():

    auction = "y"
    while auction == "y":
        biddings = []
        bidding_proccess = "y"
        while bidding_proccess == "y":
            clear_terminal()
            print("Welcome to a secret AUCTION.\nPlease follow the instructions")
            print(COMMON_ART["divider"])
            print(TASK_ART["title"])
            print(COMMON_ART["divider"])
            name = input("Fill out your complete name:\n - ")
            bid_amount = validate_int(
                "For this article, how much are you bidding?\n - $"
            )
            biddings.append(bidding(name, bid_amount))
            print("Thank you for your bid, GOOD LUCK!")
            bidding_proccess = validate_input(
                "Is there another bidder? Type 'y' or 'n'\n - ", ["y", "n"]
            )

        clear_terminal()
        winning_bid, winning_name = find_highest_bidder(biddings)

        loading_animation(3)
        print(f"with a bid of ${winning_bid}, {winning_name} is the WINNER!")
        print(COMMON_ART["divider"])
        auction = validate_input(
            "Is there another item in the auction? Type 'y' or 'n'\n - ", ["y", "n"]
        )


if __name__ == "__main__":
    main()
