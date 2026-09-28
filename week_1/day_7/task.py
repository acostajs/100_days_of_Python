# This is Day 7 of 100 days of Python

from .task_art import TASK_ART
from common.common_art import COMMON_ART
from .utils import random_word, print_intro


def main():
    word_to_guess = random_word()
    guess = len(word_to_guess) * "_"
    attempts = 0
    lives = 5
    guesses = ""
    guesses_list = list(guesses)

    print(TASK_ART["title"])
    print_intro()

    while guess != word_to_guess and lives != 0:
        print(f"----------------- {lives} LIVES LEFT -----------------------")
        if attempts == 0:
            print(TASK_ART["start"])
        else:
            print(TASK_ART[f"fail_{attempts}"])

        print(f"Word to guess: {guess}")
        print(f"Attempts: {guesses}")
        user_input = str(input("Guess a letter: - "))

        if user_input not in word_to_guess:
            attempts += 1
            lives -= 1
            print(
                f"\nYou've guessed {user_input}, that's not in the word. You loose a life.\n"
            )
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
        print(COMMON_ART["game_over"])
        print(f"The word was: {word_to_guess}")
    else:
        print(f"Word to guess: {guess}")
        print("You've guessed the word!! YOU WIN!!")


if __name__ == "__main__":
    main()
