import random
import string


def password_generator(
    amount_letters: int, amount_digits: int, amount_symbols: int
) -> str:
    """
    Receives amount of letters, amount of digits and amount of symbols that the new password is
    going to have.
    Gives back the password in string format.
    """
    letters = list(string.ascii_letters)
    digits = list(string.digits)
    symbols = list(string.punctuation)

    characters = (
        random.choices(letters, k=amount_letters)
        + random.choices(digits, k=amount_digits)
        + random.choices(symbols, k=amount_symbols)
    )

    random.shuffle(characters)

    return "".join(characters)
