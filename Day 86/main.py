import tkinter as tk
from tkinter import messagebox
from random import shuffle
from time import time
from library import words

shuffle(words)
list_of_words = words
COUNT = 0
start: time
end: time


def start_timer(event):
    global start
    start = time()


def count_the_word(event):
    global COUNT
    global list_of_words
    global start
    global end

    word = entry_box.get()
    entry_box.delete(0, tk.END)

    if word.strip() == list_of_words[0]:
        time_elapsed = time() - start
        if time_elapsed > 60:
            messagebox.showinfo(title='Great!!!',
                                message=f"Your typing speed is {'%.2f' % (COUNT/(time_elapsed / 60))} wpm")
            window.destroy()

        COUNT += 1
        list_of_words = list_of_words[1:]

        text_area.config(state='normal')
        text_area.delete('1.0', tk.END)
        text_area.insert(tk.END, ' '.join(list_of_words))
        text_area.config(state='disabled')


window = tk.Tk()
window.config(pady=5, padx=20)

text_area = tk.Text(height=2, width=30, font=('', 15), padx=5, pady=5)
text_area.insert(tk.END, ' '.join(list_of_words))
text_area.config(state='disabled')
text_area.grid(row=0, padx=5, pady=5)

entry_box = tk.Entry(width=73)
entry_box.grid(row=1)

entry_box.bind('<FocusIn>', start_timer)
entry_box.bind('<space>', count_the_word)

window.mainloop()
