def compare_choices(user_choice: str, computer_choice: str) -> str:
    """
    Receives the choices from the user and the computer,
    Returns message.
    """
    tie_message = "It's a TIE! Try again!"
    loose_message = "You LOOSE! Try again!"
    win_message = "CONGRATULATIONS! YOU WIN!"

    if user_choice == computer_choice:
        return tie_message
    elif (
        user_choice == "rock"
        and computer_choice == "paper"
        or user_choice == "scissors"
        and computer_choice == "rock"
        or user_choice == "paper"
        and computer_choice == "scissors"
    ):
        return loose_message
    else:
        return win_message
