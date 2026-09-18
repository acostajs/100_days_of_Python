# This is Day 8 of 100 days of Python

import string

from ascii_art import ascii_art

def encode_decode(message: str, shift: int, operation: str) -> str:
    """
        This functions works to encrypt or decrypt a message based on three parameters:
        message - message to encrypt
        shift - number of letter displacement for encryption or decryption.
        operation - to determine direction of letter displacement for decryption based on the operation choosen by the user.
    """
    alphabet = list(string.ascii_lowercase)
    digits = string.digits
    symbols = string.punctuation
    encoded_word = ""
    
    shift_operation = shift
    if operation == "decode":
        shift_operation *= -1
        
    for letter in message:
        if letter in digits or letter in symbols or letter == " ":
            encoded_word += letter
        else:
            shifted_position = alphabet.index(letter) + shift_operation
            shifted_position %= len(alphabet)                
            encoded_word += alphabet[shifted_position]
                
    return encoded_word

def loop_message(message: str, message2: str, optional_message: bool, option1: str, option2: str) -> str: 
    """
        Helper function to loop through a user input to validate user answer.
    """
    user_choice = ""
    while user_choice != option1 and user_choice != option2:
        user_choice = input(f'{message}\n - ').lower()
        if optional_message == True and user_choice != option1:
            print(f"{message2}")

        if user_choice != option1 and user_choice != option2:
            print(f"{user_choice} is not an option")
            
    return user_choice

def main():
    """
        Runs Caesar Cypher script.
    """
    user_input = "yes" 
    print(ascii_art("title"))
    
    while user_input == "yes":
        print(ascii_art("divider"))
        operation = loop_message('Type "encode" to encrypt, type "decode" to decrypt:', "", False, "encode", "decode")
        message = input("Type your message:\n - ").lower()
        shift = input("Type your shift number:\n - ").lower()
       
        encoded_word = encode_decode(message, int(shift), operation)

        if operation == "encode":
            print(f"Here's the encoded result: {encoded_word}")
        elif operation == "decode":
            print(f"Here's the decoded result: {encoded_word}")
            

        user_input = loop_message('Type "yes" if you want to go again. Otherwise type "no".', "Goodbye!", True, "yes", "no")
        
if __name__ == "__main__":
    main()
