import unittest
from quiz import Quiz, Question, Réponse

class TestQuiz(unittest.TestCase):
    def setUp(self):
        question1 = Question("Quelle est la capitale de la France?", [Réponse("Paris", True), Réponse("Berlin", False), Réponse("Londres", False)])
        question2 = Question("Quelle est la couleur du ciel?", [Réponse("Bleu", True), Réponse("Rouge", False), Réponse("Vert", False)]
        self.questions = [question1, question2]
        self.quiz = Quiz(self.questions)

    def test_score_initialization(self):
        self.assertEqual(self.quiz.score, 0)

    def test_incorrect_responses_initialization(self):
        self.assertEqual(self.quiz.incorrect_responses, [])

    def test_shuffle_questions(self):
        original_order = [q.question_text for q in self.questions]
        self.quiz.shuffle_questions()
        shuffled_order = [q.question_text for q in self.quiz.questions]
        self.assertNotEqual(original_order, shuffled_order)

    def test_correct_answer(self):
        question = self.questions[0]
        user_answer = 'a'
        self.assertTrue(self.quiz.is_answer_correct(question, user_answer))

    def test_incorrect_answer(self):
        question = self.questions[0]
        user_answer = 'b'
        self.assertFalse(self.quiz.is_answer_correct(question, user_answer))

if __name__ == '__main__':
    unittest.main()









