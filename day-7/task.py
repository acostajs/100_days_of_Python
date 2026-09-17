# This is Day 7 of 100 days of Python

import random

"""
This is the task for Day 7 of 100 days of Python.
The script recreates a simple game of Hangman.
"""

def ascii_art(input: str) -> str:
    """
    Chooses the ascii_art.
    """

    ascii_art = ""
    match input:
        case "title":
            return '''
 _                                             
| |                                            
| |__   __ _ _ ___  ____ _ __ ___   __ _ _ ___  
| '_  || _` | '_  |/ __ | '_ ` _  |/ _` | '_  | 
| | | ||(_| | | | | (_| | | | | | | (_| | | | |
|_| |_||__,_|_| |_||__, |_| |_| |_||__,_|_| |_|
                    __/ |                      
                   |____|
'''

        case "start":
            return'''               
      _______
     |/      |
     |      
     |      
     |       
     |       
     |
    _|___
'''

        case "fail_1":
            return'''               
      _______
     |/      |
     |      (_)
     |      
     |       
     |       
     |
    _|___
'''
        case "fail_2":
            return '''               
      _______
     |/      |
     |      (_)
     |    >--|--<
     |       
     |       
     |
    _|___
'''
        case "fail_3":
            return '''               
      _______
     |/      |
     |      (_)
     |    >--|--<
     |       |
     |       
     |
    _|___
'''
        case "fail_4":
            return '''               
      _______
     |/      |
     |      (_)
     |    >--|--<
     |      .|.
     |     _| |_
     |
    _|___
'''
        case "game_over":
            return '''
                
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⢀⣤⣤⣤⣶⣶⣷⣤⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣶⣶⠀⠀⠀⠀⣠⣾⣿⣿⡇⠀⣿⣿⣿⣿⠿⠛⠉⠉⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⠀⠀⠀⠀⠀⢀⣿⣿⣶⡀⠀⠀⠀⠀⠀⣾⣿⣿⣿⡄⠀⢀⣴⣿⣿⣿⣿⠁⢸⣿⣿⣿⣀⣤⡀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⣼⣿⣿⣿⣧⠀⠀⠀⠀⢰⣿⣿⣿⣿⣇⣠⣿⣿⣿⣿⣿⡏⢠⣿⣿⣿⣿⣿⡿⠗⠂⠀⠀
⠀⠀⠀⣰⣾⣿⣿⠟⠛⠉⠉⠉⠉⠋⠀⠀⠀⣰⣿⣿⣿⣿⣿⣇⣠⣤⣤⣿⣿⣿⢿⣿⣿⣿⣿⢿⣿⣿⡿⠀⣼⣿⣿⡟⠉⠁⢀⣀⡄⠀⠀
⠀⢀⣾⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣴⣿⣿⣿⣿⡿⣿⣿⣿⡏⠈⢿⣿⣿⠏⣾⣿⣿⠃⢠⣿⣿⣿⣶⣶⣿⣿⣿⡷⠦⠀
⢠⣾⣿⡿⠀⠀⠀⣀⣠⣴⣶⣿⣿⡷⠀⣠⣿⣿⣿⣿⡿⠟⣿⣿⣿⣠⣿⣿⣿⠀⠀⠀⠀⠁⢸⣿⣿⡏⠀⣼⣿⣿⣿⠿⠛⠛⠉⠀⠀⠀⠀
⢸⣿⣿⠣⣴⣾⣿⣿⣿⣿⣿⣿⡿⠃⣰⣿⣿⣿⠋⠁⠀⠀⠸⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠸⠿⠿⠀⠀⠛⠛⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⣿⣿⣆⣉⣻⣭⣿⣿⣿⡿⠋⠀⠀⢿⣿⡿⠁⠀⠀⠀⠀⠀⠹⠟⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠙⠿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣶⣶⣶⣶⣦⣄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣷⠄⣤⣤⣤⣤⣶⣾⣷⣴⣿⣿⣿⣿⠿⠿⠛⣻⣿⣿⣷⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣄⠀⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠋⢠⣿⣿⣿⠿⠛⠋⠉⠛⣿⣿⣿⠏⢀⣤⣾⣿⣿⡿⠋⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⠓⢹⣿⣿⣷⠀⠀⠀⠀⢀⣶⣿⡿⠁⠀⣾⣿⣿⣟⣠⣤⠀⠀⢸⣿⣿⣿⣾⣿⣿⣿⡟⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⡿⠛⠉⠸⣿⣦⡈⣿⣿⣿⡇⠀⠀⣰⣿⣿⡿⠁⠀⢸⣿⣿⣿⣿⣿⠿⠷⢀⣿⣿⣿⣿⡿⠛⣿⣿⣿⡀⠀⠀⠀
⠀⠀⠀⠀⢀⣼⣿⣿⡿⠋⠀⠀⠀⠀⣿⣿⣧⠘⣿⣿⣿⡀⣼⣿⣿⡟⠀⠀⢀⣿⣿⣿⠋⠁⠀⣀⣀⣼⣿⣿⡟⠁⠀⠀⠘⣿⣿⣧⠀⠀⠀
⠀⠀⠀⠀⣼⣿⣿⡟⠀⠀⠀⠀⠀⣠⣿⣿⣿⠀⢹⣿⣿⣿⣿⣿⡟⠀⠀⠀⣼⣿⣿⣷⣶⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠸⣿⣿⡆⠀⠀
⠀⠀⠀⠀⢹⣿⣿⣇⠀⠀⢀⣠⣴⣿⣿⣿⡿⠀⠈⣿⣿⣿⣿⡟⠀⠀⠀⢰⣿⣿⣿⠿⠟⠛⠉⠁⠸⢿⡟⠀⠀⠀⠀⠀⠀⠀⠘⠋⠁⠀⠀
⠀⠀⠀⠀⠈⢻⣿⣿⣿⣾⣿⣿⣿⣿⣿⠟⠁⠀⠀⠸⣿⣿⡿⠁⠀⠀⠀⠈⠙⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠛⠿⠿⠿⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''

        case "divider":
            return '''
----------------------------------------------------------------------                
'''

    return ascii_art

def random_word() -> str:
    
    words = [
        "python",
        "keyboard",
        "elephant",
        "guitar",
        "mountain",
        "sandwich",
        "umbrella",
        "penguin",
        "volcano",
        "bicycle",
        "dinosaur",
        "chocolate",
        "telescope",
        "backpack",
        "dolphin",
        "rainbow",
        "castle",
        "spaceship",
        "butterfly",
        "wizard",
    ]

    random_word = random.choice(words)
    return random_word

def print_intro():
    print(ascii_art("title"))
    print(ascii_art("divider"))
    print('''Welcome to HANGMAN!\n
          The game where you have to guess the word one letter at a time.\n
          Instructions:\n
          1) Input the letter.
          2) If the letter is correct its going to fill the blank space where the letter is placed.
          3) If the letter is not correct, you loose one try.
          4) You can get up to 5 wrong letters, the 6th is game over.
          ''')
    print(ascii_art("divider"))
    
def main():
    word_to_guess = random_word()
    guess = len(word_to_guess) * "_"
    attempts = 0
    lives = 5
    guesses = ""
    guesses_list = list(guesses)
        
    print_intro()

    while guess != word_to_guess and lives != 0:
        
        print(f'----------------- {lives} LIVES LEFT -----------------------')
        if attempts == 0:
            print(ascii_art("start"))
        else:
            print(ascii_art(f"fail_{attempts}"))

        print(f'Word to guess: {guess}')
        print(f"Attempts: {guesses}")
        user_input = str(input("Guess a letter: - "))
        
        if user_input not in word_to_guess:
            attempts += 1
            lives -= 1
            print(f"\nYou've guessed {user_input}, that's not in the word. You loose a life.\n")
        elif user_input in guesses:
            print(f"\nYou've already guessed {user_input}\n")
        else:
          
            print(f"\n{user_input} is in the word.\n")
            guess_list = list(guess)
            for index, letter in enumerate(word_to_guess):
                  if user_input == letter:
                      guess_list[index] = user_input

            guess = "".join(guess_list)    

        guesses_list.append(user_input)
        guesses = "".join(guesses_list)                

        
    if lives == 0:
        print(ascii_art("game_over"))
        print(f"The word was: {word_to_guess}")
    else:
        print(f"Word to guess: {guess}")
        print("You've guessed the word!! YOU WIN!!")
        
        
if __name__== "__main__":
    main()
