import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
LIGHT_GREEN = "#afc8ad"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
TICK_MARK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
total_ticks = 0
timer = ''


# ---------------------------- TIMER RESET ------------------------------- #
def reset_countdown():
    global reps
    global total_ticks

    window.after_cancel(timer)
    timer_label.config(text='TIMER')
    canvas.itemconfig(timer_text, text='00:00')
    reps = 0
    total_ticks = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_countdown():
    global reps
    global total_ticks

    reps += 1

    if reps % 8 == 0:
        timer_label.config(text='Break', fg=RED)
        countdown(LONG_BREAK_MIN * 60)
        total_ticks = 0
    elif reps % 2 == 0:
        timer_label.config(text='Break', fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(text='Work', fg=GREEN)
        countdown(WORK_MIN * 60)

    tick_label.config(text=TICK_MARK*total_ticks)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global total_ticks
    global timer

    timer_min = int(count // 60)
    if timer_min < 10:
        timer_min = f'0{timer_min}'
    timer_sec = int(count % 60)
    if timer_sec < 10:
        timer_sec = f'0{timer_sec}'
    canvas.itemconfig(timer_text, text=f'{timer_min}:{timer_sec}')
    if count > 0:
        timer = window.after(1000, countdown, count-1)
    else:
        start_countdown()
        if reps % 2 == 0:
            total_ticks += 1


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_photo = tk.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_photo)
timer_text = canvas.create_text(105, 130, text='00:00', fill='white', font=(FONT_NAME, 34, 'bold'))
canvas.grid(column=1, row=1)

timer_label = tk.Label(text='TIMER', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 34, 'bold'))
timer_label.grid(column=1, row=0)

start_button = tk.Button(text='Start', padx=20, pady=5, bg=LIGHT_GREEN, activebackground=GREEN, command=start_countdown)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text='Reset', padx=20, pady=5, bg=LIGHT_GREEN, activebackground=GREEN, command=reset_countdown)
reset_button.grid(column=2, row=2)

tick_label = tk.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
tick_label.grid(column=1, row=3)

window.mainloop()
