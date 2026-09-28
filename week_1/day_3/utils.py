
from common.validators import validate_input
from common.common_art import COMMON_ART


def check_step(prompt: str, options: list[str], correct_answer: str, fail_message: str) -> bool:
    answer = validate_input(prompt, options)
    if answer != correct_answer:
        print(f"{fail_message}")
        print(COMMON_ART["game_over"])
        return False
    return True

