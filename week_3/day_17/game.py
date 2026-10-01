from random import choice


class Game:
    def __init__(self, questions):
        self.questions = questions
        self.messages = {"correct": "You got it right!", "wrong": "That's wrong"}

    def random_question(self):
        random_question = choice(self.questions)
        question = random_question["question"]
        answer = random_question["answer"]
        return question, answer

    def check_answer(self, answer, user_answer):
        if user_answer == answer:
            message = "correct"
            return message, True
        else:
            message = "wrong"
            return message, False

    def print_message(self, message):
        print(self.messages[message])

    def ask_question(self, user, question):
        user.asked_questions += 1
        print(f"Q.{user.asked_questions}: {question} - True/False:")

    def play(self, user, question_quantity):
        print("Welcome to a quiz game!")
        while question_quantity > user.asked_questions:
            question, answer = self.random_question()
            self.ask_question(user, question)
            user_answer = user.answer()
            message, is_answer_correct = self.check_answer(answer, user_answer)
            self.print_message(message)
            user.update_score(is_answer_correct)
            user.print_score("current score")

        user.print_score("final score")
