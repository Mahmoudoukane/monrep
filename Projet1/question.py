# question.py

class Question:
    def __init__(self, question_text, answers):
        self.question_text = question_text
        self.answers = answers

    def shuffle_answers(self):
        import random
        random.shuffle(self.answers)

class Réponse:
    def __init__(self, text, correct=False):
        self.text = text
        self.correct = correct















