import string


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
