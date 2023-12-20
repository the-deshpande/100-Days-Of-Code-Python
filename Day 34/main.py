from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = list()
for item in question_data:
    question_bank.append(Question(item['question'], item['correct_answer']))

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
