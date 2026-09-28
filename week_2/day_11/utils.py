# This are the helper functions for task.py of Day 11 of 100 days of Python.

import random
import time
from .data import cards
from .task_art import TASK_ART


def random_card() -> dict:
    random_card = random.choice(cards)

    return random_card


def deal(number_of_cards: int) -> list[dict]:
    cards = []
    for _ in range(number_of_cards):
        time.sleep(0.5)
        card = random_card()
        cards.append(card)
        print(TASK_ART[card["name"]])

    return cards


def calculate_score(cards: list[dict]) -> int:
    score = 0
    aces = 0

    for card in cards:
        if card["name"] == "ace":
            aces += 1
            score += 11
        else:
            score += card["value"]

    while score > 21 and aces > 0:
        score -= 10
        aces -= 1

    return score


def print_result(
    message: str,
    user_cards: list,
    user_score: int,
    computer_cards: list,
    computer_score: int,
):
    print(f"Your cards: {card_names(user_cards)}, your score: {user_score}")
    print(
        f"Computer cards: {card_names(computer_cards)}, computer score: {computer_score}"
    )
    print(message)


def card_names(cards: list[dict]) -> list[str]:
    return [card["name"] for card in cards]
