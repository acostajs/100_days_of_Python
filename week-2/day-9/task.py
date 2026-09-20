# This is Day 9 of 100 days of Python

import os
import time
import string

from ascii_art import ascii_art


def bidding(name: str, bid_amount: int) -> dict:
    bid = {
        "name": name,
        "bid": bid_amount
    }
    return bid

def loading_animation(frames: int):
    print(ascii_art("title"))   
    print(ascii_art("divider"))
    
    for frame in range(frames):
        time.sleep(frame)
        match frame:
            case 0:
                print("Going ONCE!")
            case 1:
                print("Going TWICE!")
            case 2:
                print("SOLD to the highest bidder!!")

def main():
    
    print("Welcome to a secret bidding.\nPlease follow the instructions")
    biddings = []
    bidding_proccess = "yes"
    while bidding_proccess == "yes":
        print(ascii_art("divider"))
        print(ascii_art("title"))
        print(ascii_art("divider"))
        name = input("Fill out your complete name:\n - ")
        bid_amount = int(input("For this article, how much are you bidding?\n - $"))
        biddings.append(bidding(name, bid_amount))
        print("Thank you for your bid, GOOD LUCK!")
        bidding_proccess = input("""Is there another bidder? Type 'yes' or 'no'\n - """)
        os.system('csl' if os.name == 'nt' else 'clear')

    winning_bid = 0
    
    for bid in range(len(biddings)):
        new_bid = biddings[bid]["bid"]
        if new_bid > winning_bid:
            winning_bid = new_bid
            winning_name = biddings[bid]["name"]

    loading_animation(3)
    print(f"with a bid of ${winning_bid}, {winning_name} is the WINNER!")

    
if __name__ == "__main__":
    main()
