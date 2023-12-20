import html


class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0
        self.curr_question = self.question_list[0]

    def next_question(self):
        self.curr_question = self.question_list[self.question_number]
        self.question_number += 1
        return f'Q.{self.question_number}: {html.unescape(self.curr_question.text)}'

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer):
        correct_answer = self.curr_question.answer
        if answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        return False
