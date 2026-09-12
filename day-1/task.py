# This is day 1 of 100 days of Python

"""
This script runs the code for day 1 of 100 days of Python.
It prompts the user to enter their city of birth and the name of their first pet,
then prints a sentence combining these inputs.
"""

def main():
    name = input("Hi! what is your name? : ")
    name_length = len(name)
    print(f"{name}, this is your band name generator\nLet's start with a couple of questions.")
    city = input("1. What city were you born in? : ")
    pet = input("2. What was the name of your first pet? : ")
    number = input("3. Choose a number between 1 and 10: ")
    band_number = name_length * int(number)
    print(f"Now, your name has {name_length} characters times {number} is {band_number}")
    print(f"{name}, your band name is {city} {pet} {band_number}")

if __name__ == "__main__":
    main()
