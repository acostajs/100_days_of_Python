# This are the helper functions for task.py of Day 11 of 100 days of Python.

import random
import time

from ascii_art import ascii_art


def random_card() -> dict:        
    cards = [
        {"name": "ace", "value": [1, 11]},
        {"name": "2", "value": 2},
        {"name": "3", "value": 3},
        {"name": "4", "value": 4},
        {"name": "5", "value": 5},
        {"name": "6", "value": 6},
        {"name": "7", "value": 7},
        {"name": "8", "value": 8},
        {"name": "9", "value": 9},
        {"name": "jack", "value": 10},
        {"name": "queen", "value": 10},
        {"name": "king", "value": 10}
    ]

    random_card = random.choice(cards)

    return random_card

def validate_input(prompt: str, choices: set) -> str:
    valid_choices = choices
    choice = input(prompt)
    while choice not in valid_choices:
        choice = input(f"Wrong input: Type {valid_choices}:\n - ")

    return choice

def deal(number_of_cards: int) -> list[dict]:
    cards = []
    for _ in range(number_of_cards):
        time.sleep(0.5)
        card = random_card()
        cards.append(card)
        print(ascii_art(card["name"]))
        
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

def print_result(message: str, user_cards: list, user_score: int, computer_cards: list, computer_score: int):
    print(f"Your cards: {card_names(user_cards)}, your score: {user_score}")
    print(f"Computer cards: {card_names(computer_cards)}, computer score: {computer_score}")
    print(message)

def card_names(cards: list[dict]) -> list[str]:
    return [card["name"] for card in cards]
