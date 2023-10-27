from question import Question, Réponse
import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.incorrect_responses = []

    def shuffle_questions(self):
        random.shuffle(self.questions)

    def run(self):
        self.shuffle_questions()

        for i, question in enumerate(self.questions, start=1):
            self.display_question(question, i)
            user_answer = self.get_user_answer()
            if self.check_answer(question, user_answer):
                self.handle_correct_answer()
            else:
                self.handle_incorrect_answer(question, user_answer)

        self.display_correction_and_score()

    def display_question(self, question, question_number):
        question.shuffle_answers()
        print(f"Question {question_number}: {question.question_text}")
        for i, answer in enumerate(question.answers, start=1):
            print(f"{chr(96 + i)}) {answer.text}")

    def get_user_answer(self):
        while True:
            user_answer = input("Votre réponse (a/b/c) : ").strip().lower()
            if user_answer in ['a', 'b', 'c']:
                return user_answer
            else:
                print("Réponse invalide. Veuillez répondre en utilisant 'a', 'b', ou 'c'.")

    def check_answer(self, question, user_answer):
        user_choice = ord(user_answer) - ord('a')
        return question.answers[user_choice].correct

    def handle_correct_answer(self):
        print("Correct!\n")
        self.score += 1

    def handle_incorrect_answer(self, question, user_answer):
        self.incorrect_responses.append((question, user_answer))
        print("Réponse incorrecte.\n")

    def display_correction_and_score(self):
        print("\nCorrection des réponses incorrectes :")
        for i, (question, user_answer) in enumerate(self.incorrect_responses, start=1):
            self.display_question(question, i)
            print(f"Votre réponse : {question.answers[ord(user_answer) - ord('a')].text}")
            correct_answer_text = next(answer.text for answer in question.answers if answer.correct)
            print(f"Réponse correcte : {correct_answer_text}\n")

        self.display_score()

    def display_score(self):
        print(f"Score final : {self.score}/{len(self.questions)}")

if __name__ == "__main__":
    question1 = Question("Quelle est la capitale de la France ?", [Réponse("Paris", True), Réponse("Berlin", False), Réponse("Londres", False)])
    question2 = Question("Quelle est la couleur du ciel ?", [Réponse("Bleu", True), Réponse("Rouge", False), Réponse("Vert", False)])
    question3 = Question("Quelle est la capitale de l'Espagne ?", [Réponse("Madrid", True), Réponse("Rome", False), Réponse("Amsterdam", False)])
    question4 = Question("Quel est l'organe principal du système respiratoire ?", [Réponse("Poumon", True), Réponse("Cœur", False), Réponse("Foie", False)])
    question5 = Question("Combien de planètes y a-t-il dans notre système solaire ?", [Réponse("8", True), Réponse("7", False), Réponse("9", False)])
    question6 = Question("Quel est l'inventeur de la théorie de la relativité ?", [Réponse("Albert Einstein", True), Réponse("Isaac Newton", False), Réponse("Galilée", False)])
    question7 = Question("Quel est le plus grand animal terrestre ?", [Réponse("Éléphant", True), Réponse("Girafe", False), Réponse("Hippopotame", False)])
    question8 = Question("Quelle est la plus grande planète du système solaire ?", [Réponse("Jupiter", True), Réponse("Mars", False), Réponse("Saturne", False)])
    question9 = Question("Combien de côtés a un triangle équilatéral ?", [Réponse("3", True), Réponse("4", False), Réponse("5", False)])
    question10 = Question("Quel est le plus long fleuve du monde ?", [Réponse("Le Nil", True), Réponse("L'Amazone", False), Réponse("Le Mississippi", False)])

    questions = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10]

    quiz = Quiz(questions)
    quiz.run()














































