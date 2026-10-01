from common.validators import validate_input


class User:
    def __init__(self):
        self.score = 0
        self.asked_questions = 0

    def answer(self):
        user_answer = validate_input(" - ", ["true", "false"])
        return user_answer

    def update_score(self, is_answer_correct):
        if is_answer_correct:
            self.score += 1

    def print_score(self, step):
        print(f"Your {step} is: {self.score}/{self.asked_questions}")
