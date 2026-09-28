from time import sleep
from common.common_art import COMMON_ART
from .task_art import TASK_ART


def bidding(name: str, bid_amount: int) -> dict:
    bid = {"name": name, "bid": bid_amount}
    return bid


def loading_animation(frames: int):
    print(TASK_ART["title"])
    print(COMMON_ART["divider"])

    for frame in range(frames):
        sleep(frame)
        match frame:
            case 0:
                print("Going ONCE!")
            case 1:
                print("Going TWICE!")
            case 2:
                print("SOLD to the highest bidder!!")


def find_highest_bidder(biddings: list[dict]):
    winning_bid = 0
    winning_name = ""
    for bid in biddings:
        new_bid = bid["bid"]
        if new_bid > winning_bid:
            winning_bid = new_bid
            winning_name = bid["name"]

    return winning_bid, winning_name
