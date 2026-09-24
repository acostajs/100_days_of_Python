# This is Day 11 of 100 days of Python

import os


from ascii_art import ascii_art
from helpers import *

def main():
    blackjack = 21
    while True:    
        game = validate_input("Do you want to play a game of BlackJack? Type 'y' or 'n':\n - ", { "y", "n"})
        if game == 'n':
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
        
        print(ascii_art("title"))
        print(ascii_art("divider"))
        user_cards = deal(2)
        user_score = calculate_score(user_cards)
        print(f"Your cards: {card_names(user_cards)}, current score: {user_score}")
        computer_cards = deal(1)
        computer_score = calculate_score(computer_cards)
        print(f"Computer's first card: {card_names(computer_cards)}")

        pass_or_play = "y"
        while pass_or_play == 'y' and user_score < blackjack:
            pass_or_play = validate_input("Type 'y' to get another card, type 'n' to pass:\n - ", {"y", "n"})
            if pass_or_play == "y":
                user_cards += deal(1)
                user_score = calculate_score(user_cards)
                print(f"Your cards: {card_names(user_cards)}, current score: {user_score}")

        if user_score == blackjack:
            print_result("You got BLACKJACK!, You WIN!", user_cards, user_score, computer_cards, computer_score)
        elif user_score > blackjack:
            print_result("You went over. You LOSE!", user_cards, user_score, computer_cards, computer_score)
        else:
            while computer_score <= user_score and computer_score < blackjack:
                computer_cards += deal(1)
                computer_score = calculate_score(computer_cards)

            if computer_score > blackjack:
                print_result("Computer went over. YOU WIN!", user_cards, user_score, computer_cards, computer_score)
            elif computer_score == user_score:                                
                print_result("You TIED!, Good luck next time!", user_cards, user_score, computer_cards, computer_score)
            elif computer_score > user_score:                
                print_result("Computer WON!, you LOSE!", user_cards, user_score, computer_cards, computer_score)
            else:
                print_result("YOU WIN!!", user_cards, user_score, computer_cards, computer_score)

        
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ascii_art("goodbye"))    



if __name__ == "__main__":
    main()
