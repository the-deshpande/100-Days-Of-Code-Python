import tkinter as tk
from tkinter import messagebox
from password_generator_day5 import generate
import pyperclip

FONT = ('Ariel', 12)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    password = generate()
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    info = [website_entry.get(), email_entry.get(), password_entry.get()]

    if len(info[0]) == 0 or len(info[2]) == 0 or len(info[1]) == 0:
        messagebox.showinfo(title='Oops', message="Please don't leave any field empty")
        return

    is_ok = messagebox.askokcancel(title=info[0], message=f'These are the details entered:\n'
                                                          f'Email: {info[1]}\n'
                                                          f'Password: {info[2]}\n'
                                                          f'Is is okay to save?')

    if not is_ok:
        return

    with open('data.txt', 'a') as file:
        file.write(f"{info[0]} | {info[1]} | {info[2]}")
    pyperclip.copy(info[2])
    website_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Password manager')
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
logo = tk.PhotoImage(file='./logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = tk.Label(text='Website: ', font=FONT, anchor='e', width=15)
website_label.grid(column=0, row=1, pady=5)

email_label = tk.Label(text='Email/Username: ', font=FONT, anchor='e', width=15)
email_label.grid(column=0, row=2, pady=5)

password_label = tk.Label(text='Password: ', font=FONT, anchor='e', width=15)
password_label.grid(column=0, row=3, pady=5)

website_entry = tk.Entry(width=46)
website_entry.grid(column=1, row=1, columnspan=2, sticky='E', pady=5)
website_entry.focus()

email_entry = tk.Entry(width=46)
email_entry.grid(column=1, row=2, columnspan=2, sticky='E', pady=5)
email_entry.insert(0, 'dummy@email.com')

password_entry = tk.Entry(width=27)
password_entry.grid(column=1, row=3, padx=0, sticky='E', pady=5)

password_button = tk.Button(text='Generate Password', width=15, command=password_generator)
password_button.grid(column=2, row=3, padx=0, sticky='W', pady=5)

add_button = tk.Button(text='Add', width=39, command=save_info)
add_button.grid(column=1, row=4, columnspan=2, sticky='E', pady=5)

window.mainloop()
