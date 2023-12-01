class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f'Q.{self.question_number}: {question.text} (True/False) : ')
        self.check_answer(answer,question.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self,answer,correct_answer):
        print(f'The correct answer is : {correct_answer}')
        if answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"You're score is {self.score}/{self.question_number}\n")
