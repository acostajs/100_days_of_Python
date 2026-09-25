# This is day 14 of 100 days of Python

from common.ascii_art import ascii_art
from common.validators import validate_input
from common.toolkit import clear_terminal
from utils import random_celebrities

def main():
    
    
    celebrities = [
        {"name": "Cristiano Ronaldo", "known_for": "Widely considered one of the greatest footballers ever", "followers": 672, "origin": "Portugal"},
        {"name": "Lionel Messi", "known_for": "Argentine footballer, multiple Ballon d'Or winner", "followers": 515, "origin": "Argentina"},
        {"name": "Selena Gomez", "known_for": "Singer, actress, and beauty entrepreneur", "followers": 415, "origin": "United States"},
        {"name": "Kylie Jenner", "known_for": "Businesswoman and reality TV star", "followers": 390, "origin": "United States"},
        {"name": "Dwayne \"The Rock\" Johnson", "known_for": "Actor and former WWE wrestler", "followers": 390, "origin": "United States"},
        {"name": "Ariana Grande", "known_for": "Pop singer and actress", "followers": 371, "origin": "United States"},
        {"name": "Kim Kardashian", "known_for": "Media personality and businesswoman", "followers": 353, "origin": "United States"},
        {"name": "Beyoncé", "known_for": "Singer and cultural icon", "followers": 307, "origin": "United States"},
        {"name": "Khloé Kardashian", "known_for": "Media personality and businesswoman", "followers": 299, "origin": "United States"},
        {"name": "Justin Bieber", "known_for": "Pop singer", "followers": 292, "origin": "Canada"},
        {"name": "Kendall Jenner", "known_for": "Model", "followers": 284, "origin": "United States"},
        {"name": "Taylor Swift", "known_for": "Pop/country singer-songwriter, one of the best-selling artists ever", "followers": 281, "origin": "United States"},
        {"name": "Virat Kohli", "known_for": "Indian cricket legend", "followers": 273, "origin": "India"},
        {"name": "Kourtney Kardashian", "known_for": "Reality TV star and entrepreneur", "followers": 224, "origin": "United States"},
        {"name": "Neymar Jr.", "known_for": "Brazilian football star", "followers": 218, "origin": "Brazil"},
        {"name": "Katy Perry", "known_for": "Pop singer", "followers": 210, "origin": "United States"},
        {"name": "Jennifer Lopez", "known_for": "Singer, actress, and dancer", "followers": 250, "origin": "United States"},
        {"name": "Nicki Minaj", "known_for": "Rapper", "followers": 230, "origin": "Trinidad and Tobago"},
        {"name": "Miley Cyrus", "known_for": "Singer and actress", "followers": 215, "origin": "United States"},
        {"name": "Kevin Hart", "known_for": "Comedian and actor", "followers": 180, "origin": "United States"},
        {"name": "Shakira", "known_for": "Colombian singer", "followers": 130, "origin": "Colombia"},
        {"name": "Rihanna", "known_for": "Singer and Fenty Beauty founder", "followers": 150, "origin": "Barbados"},
        {"name": "Zendaya", "known_for": "Actress, known for \"Euphoria\" and \"Dune\"", "followers": 185, "origin": "United States"},
        {"name": "Priyanka Chopra Jonas", "known_for": "Bollywood/Hollywood actress", "followers": 95, "origin": "India"},
        {"name": "Will Smith", "known_for": "Actor", "followers": 75, "origin": "United States"},
        {"name": "Vin Diesel", "known_for": "Actor, \"Fast & Furious\" franchise", "followers": 120, "origin": "United States"},
        {"name": "Ronaldinho", "known_for": "Retired Brazilian football legend", "followers": 55, "origin": "Brazil"},
        {"name": "Emma Watson", "known_for": "Actress, known for \"Harry Potter\"", "followers": 75, "origin": "United Kingdom"},
        {"name": "Billie Eilish", "known_for": "Singer-songwriter", "followers": 120, "origin": "United States"},
        {"name": "Drake", "known_for": "Rapper", "followers": 150, "origin": "Canada"},
    ] 

    attempts = 1
    score = 0

    while attempts == 1:
        choice_a, choice_b = random_celebrities(celebrities)
        print(ascii_art("higher_lower"))
        print(ascii_art("divider"))
        print(f"Compare A: {choice_a["name"]}, {choice_a["known_for"]}, from {choice_a["origin"]}")
        print(ascii_art("vs"))
        print(f"Against B: {choice_b["name"]}, {choice_b["known_for"]}, from {choice_b["origin"]}")
        
        if score > 0:
            print(f"You're RIGHT! Your current score: {score}")
            
        if choice_a["followers"] > choice_b["followers"]:
            answer = "a"
        else:
            answer = "b"
        
        user_choice = validate_input("Who has more followers? Type 'A' or 'B': - ", ['a', 'b'])
        if user_choice == answer:
            score += 1
        else:
            attempts -= 1

        clear_terminal()

    print(ascii_art("higher_lower"))
    print(ascii_art("divider"))
    print(f"Sorry, that's wrong. Final score: {score}")
    print(ascii_art("goodbye"))
        
            
if __name__ == "__main__":
    main()
