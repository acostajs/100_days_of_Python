# This is Day 8 of 100 days of Python
from .utils import encode_decode
from common.common_art import COMMON_ART
from .task_art import TASK_ART
from common.toolkit import clear_terminal
from common.validators import validate_input, validate_int


def main():

    clear_terminal()
    user_input = "yes"

    while user_input == "yes":
        print(TASK_ART["title"])
        print(COMMON_ART["divider"])
        operation = validate_input(
            'Type "encode" to encrypt, type "decode" to decrypt:\n - ',
            ["encode", "decode"],
        )
        message = input("Type your message:\n - ").lower()
        shift = validate_int("Type your shift number:\n - ")

        encoded_word = encode_decode(message, shift, operation)
        print(f"Here's the {operation} result: {encoded_word}")

        user_input = validate_input(
            'Type "yes" if you want to go again. Otherwise type "no".\n - ',
            ["yes", "no"],
        )


if __name__ == "__main__":
    main()
