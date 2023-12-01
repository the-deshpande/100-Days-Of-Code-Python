from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = list()
for item in question_data:
    question_bank.append(Question(item['question'], item['correct_answer']))

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("Congratulations! You have finished the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")