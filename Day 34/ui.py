import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = tk.Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tk.Label(text='Score: 0', bg=THEME_COLOR, fg='white', font=('Arial', 14))
        self.score_label.grid(column=1, row=0)

        self.canvas = tk.Canvas(width=300, height=250, bg='white')
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=50)

        self.question_text = self.canvas.create_text(150, 125, fill=THEME_COLOR, font=FONT, width=280)
        self.get_next_question()

        tick_photo = tk.PhotoImage(file='./images/true.png')
        self.correct_button = tk.Button(image=tick_photo, highlightthickness=0, command=self.guessed_true)
        self.correct_button.grid(column=0, row=2)

        cross_photo = tk.PhotoImage(file='./images/false.png')
        self.incorrect_button = tk.Button(image=cross_photo, highlightthickness=0, command=self.guessed_false)
        self.incorrect_button.grid(column=1, row=2)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_question():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You\'ve finished the quiz!!!')

    def guessed_true(self):
        self.display(self.quiz.check_answer('True'))

    def guessed_false(self):
        self.display(self.quiz.check_answer('False'))

    def display(self, choice):
        if choice:
            self.canvas.config(bg='green')
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, func=self.get_next_question)

