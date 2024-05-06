import tkinter as tk
from tkinter import messagebox
import pyperclip

TIMER = 5

new_call = True
timer = TIMER


def countdown(event):
    global new_call
    global timer

    if type(event) is tk.Event:
        if not new_call:
            timer = TIMER
            return
        new_call = False

    if timer == 0:
        new_call = True
        timer = TIMER

        text = text_area.get('1.0', tk.END)

        text_area.delete('1.0', tk.END)

        save_text = messagebox.askyesno(title='Want your text?', message="You wish to copy your text to clipboard?")
        if save_text:
            pyperclip.copy(text)

        return

    timer = timer-1
    window.after(1000, countdown, '')


window = tk.Tk()
window.title('Disappearing Text App')
window.config(padx=100, pady=50)

text_area = tk.Text()
text_area.config(font=("Arial", 14))
text_area.grid()

text_area.bind("<Key>", countdown)

window.mainloop()
