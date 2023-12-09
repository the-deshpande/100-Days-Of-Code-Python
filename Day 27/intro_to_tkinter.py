import tkinter as tk

window = tk.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Labels
my_label = tk.Label(text='I am a label', font=('Ariel', 24, 'bold'))
my_label['text'] = 'New Text'
my_label.config(text='Hello')
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Buttons


def button_clicked():
    print('I got clicked')
    my_label.config(text=entry.get())


my_button1 = tk.Button(text='Click Me', command=button_clicked)
my_button1.grid(column=1, row=1)

my_button2 = tk.Button(text='Button 2')
my_button2.grid(column=2, row=0)

# Entry

entry = tk.Entry()
entry.grid(column=3, row=2)

window.mainloop()
