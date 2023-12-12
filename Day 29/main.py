import tkinter as tk
from tkinter import messagebox
from password_generator_day5 import generate
import pyperclip
import json

FONT = ('Ariel', 12)


# --------------------------------- SEARCH --------------------------------------#
def search_database():
    website = website_entry.get()

    if len(website) == 0:
        messagebox.showinfo(title='Oops', message="Please don't leave website field empty")
        return

    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showinfo(title='Oops', message="No stored email or password for this website")
    else:
        if website in data.keys():
            messagebox.showinfo(title=website, message=f'These are the details entered:\n'
                                                       f'Email: {data[website]['email']}\n'
                                                       f'Password: {data[website]['password']}\n')
            pyperclip.copy(data[website]['password'])
        else:
            messagebox.showinfo(title='Oops', message="No stored email or password for this website")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password = generate()
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    website = website_entry.get()
    info = {
        website: {
            'email': email_entry.get(),
            'password': password_entry.get()
        }
    }

    if len(info[website]) == 0 or len(info[website]['email']) == 0 or len(info[website]['password']) == 0:
        messagebox.showinfo(title='Oops', message="Please don't leave any field empty")
        return

    is_ok = messagebox.askokcancel(title=info[website], message=f'These are the details entered:\n'
                                                                f'Email: {info[website]['email']}\n'
                                                                f'Password: {info[website]['password']}\n'
                                                                f'Is is okay to save?')

    if not is_ok:
        return

    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = dict()
    data.update(info)

    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

    pyperclip.copy(info[website]['password'])
    website_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Password Manager')
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

website_entry = tk.Entry(width=27)
website_entry.grid(column=1, row=1, sticky='E', pady=5)
website_entry.focus()

email_entry = tk.Entry(width=48)
email_entry.grid(column=1, row=2, columnspan=2, sticky='E', pady=5)
email_entry.insert(0, 'dummy@email.com')

password_entry = tk.Entry(width=27)
password_entry.grid(column=1, row=3, padx=0, sticky='E', pady=5)

search_button = tk.Button(text='Search', width=15, command=search_database)
search_button.grid(column=2, row=1, padx=5, sticky='W', pady=5)

password_button = tk.Button(text='Generate Password', width=15, command=password_generator)
password_button.grid(column=2, row=3, padx=5, sticky='W', pady=5)

add_button = tk.Button(text='Add', width=40, command=save_info)
add_button.grid(column=1, row=4, columnspan=2, sticky='E', pady=5)

window.mainloop()
