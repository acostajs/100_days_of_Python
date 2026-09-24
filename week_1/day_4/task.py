# This is day 4 of 100 days of Python
import random

"""
This script runs the code for day 4 of 100 days of Python.
It prompts a game of rock, paper or scissors.
Uses random choices to choose from the three options and compare it to the user answer.
"""

def print_choice(choice):
    
    if choice == "rock":
        print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    ''')
    if choice == "paper":
        print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    ''')
    if choice == "scissors":
        print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    ''')

    return (print)

def compare_choices(user_choice, computer_choice):
    tie_message = "It's a TIE! Try again!"
    loose_message = "You LOOSE! Try again!"
    win_message = "CONGRATULATIONS! YOU WIN!"
    
    if user_choice == computer_choice:
        return tie_message
    elif user_choice == "rock" and computer_choice == "paper" or user_choice == "scissors" and computer_choice == "rock" or user_choice == "paper" and computer_choice == "scissors":
        return loose_message
    else:
        return win_message

         
def main():

    choices = ["rock", "paper", "scissors"]
    
    user_choice = input("Choose between rock, paper or scissors: - ").lower()
    if user_choice not in choices:
        print(f"{user_choice} is not a possible choice, try again")
        return
    
    computer_choice = random.choice(choices)
    print(f"You've choosen {user_choice}")
    print_choice(user_choice)
    print(f"The computer choose {computer_choice}")
    print_choice(computer_choice)
    print(compare_choices(user_choice, computer_choice)) 
       

if __name__ == "__main__":
    main()
