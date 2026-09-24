# This is the helpers function for task.py for Day 12 of 100 days of Python

import random


def random_number(difficulty: str) -> int:
    """
        Receives the chosen level difficulty of the user,
        and gives back a random number between the range determined by the difficulty.
    """
    match difficulty:
        case "easy":
            random_number = random.randint(1, 10)
        case "medium":
            random_number = random.randint(1, 100)
        case "hard":
            random_number = random.randint(1, 1000)

    return random_number        

def number_of_attempts(difficulty: str) -> int:
    """
        Receives the chosen level of difficulty of the user,
        and gives back the number of the attemps based on the difficulty.
    """

    match difficulty:
        case "easy":
            attempts = 20
        case "medium":
            attempts = 15
        case "hard":
            attempts = 10

    return attempts

def validate_input(prompt: str, valid_inputs: set) -> str:
    """
        Receives prompt to ask the user and a set of valid inputs,
        it limits the result of the input to the set of valid inputs,
        else it keeps in the loop until one of the valid inputs have been written.
    """
    valid_input = input(prompt)
    while valid_input not in valid_inputs:
        valid_input = input(f"Wrong input: type {valid_inputs} ")
    return valid_input

def validate_int(prompt: str) -> int:
    """
        Validates that the user only writes integers in their answer.
    """
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print("Wrong Input: Please enter a valid integer")
            
def check_guess(number: int, total_attempts: int):
    """
        Receives the number to guess and the total number of attemps the user has for the game,
        it develops the logic of the game.
    """
    guess = 0
    attempts = total_attempts
    while attempts > 0 and guess != number:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = validate_int("Make a guess: ")

        if guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")

        if guess != number:
            attempts -= 1
            print("Guess again")

    if guess == number:
        print(f"You've GUESSED the number! it was {number}")
    if attempts == 0:
        print("Good try! good luck the next time.")
    
