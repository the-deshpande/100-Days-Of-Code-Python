import tkinter as tk

window = tk.Tk()
window.title('Miles to Kilometer')
window.config(padx=10, pady=10)


def miles_to_km():
    convert = int(entry.get()) * 1.609
    value.config(text=convert)


entry = tk.Entry()
entry.grid(column=1, row=0)

miles = tk.Label(text='Miles')
miles.grid(column=2, row=0)

is_equal_to = tk.Label(text='is equal to')
is_equal_to.grid(column=0, row=1)

value = tk.Label(text='0')
value.grid(column=1, row=1)

km = tk.Label(text='Km')
km.grid(column=2, row=1)

button = tk.Button(text='Calculate', command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()
