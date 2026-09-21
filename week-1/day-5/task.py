# This is Day 5 of 100 days of Python

import random
import string

"""
This script runs the code for day 5 of 100 days of Python.
This is a Password Generator.
"""

def main():
    letters = list(string.ascii_letters)
    digits = list(string.digits)
    symbols = list(string.punctuation)

    print("Welcome to the PyPassword Generator")
    amount_letters = int(input("How many letters would you like in your password?:\n - "))
    amount_digits = int(input("How many numbers would you like?:\n - "))
    amount_symbols = int(input("How many symbols would you like?:\n - "))

    characters = random.choices(letters, k=amount_letters)
    characters += random.choices(digits, k=amount_digits)
    characters += random.choices(symbols, k=amount_symbols)

    random.shuffle(characters)

    password = ""
    for character in characters:
        password += character

    print(f"Your password is: {password}")
    
if __name__== "__main__":
    main()
