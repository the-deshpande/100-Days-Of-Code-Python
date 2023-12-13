import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ('Ariel', 40, 'italic')
WORD_FONT = ('Ariel', 60, 'bold')
data = pd.read_csv('./data/french_words.csv')
item = data.iloc[random.randint(0, data.shape[0] - 1)]
flipper = ''

# ------------------------- DATA READING --------------------------------- #

try:
    new_data = pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('./data/french_words.csv')
else:
    if new_data.shape[0] != 0:
        data = new_data


# -------------------------  NEXT CARD ----------------------------------- #
def next_card():
    global flipper
    global data
    global item

    if data.shape[0] == 0:
        data = pd.read_csv('./data/french_words.csv')
    if flipper != '':
        window.after_cancel(flipper)

    item = data.iloc[random.randint(0, data.shape[0]-1)]
    canvas.itemconfig(card, image=front_card)
    canvas.itemconfig(title_text, text='French', fill='black')
    canvas.itemconfig(word_text, text=item['French'], fill='black')
    flipper = window.after(3000, flip_card)


def flip_card():
    global item

    canvas.itemconfig(card, image=back_card)
    canvas.itemconfig(title_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=item['English'], fill='white')


def remove_card():
    global data
    global item

    data = data[data.iloc[:, 1] != item['English']]
    data.to_csv('./data/words_to_learn.csv')

    next_card()


# ----------------------------- UI --------------------------------------- #
window = tk.Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = tk.PhotoImage(file='./images/card_front.png')
back_card = tk.PhotoImage(file='./images/card_back.png')
card = canvas.create_image(400, 263)
title_text = canvas.create_text(400, 150, font=LANGUAGE_FONT)
word_text = canvas.create_text(400, 263, font=WORD_FONT)
next_card()
canvas.grid(column=0, row=0, columnspan=2)

right_image = tk.PhotoImage(file='./images/right.png')
right_button = tk.Button(image=right_image, highlightthickness=0, command=remove_card)
right_button.grid(column=1, row=1)

wrong_image = tk.PhotoImage(file='./images/wrong.png')
wrong_button = tk.Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

window.mainloop()
