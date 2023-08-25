from tkinter import *
import math
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 10
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rounds = 0
timer_count = None
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global rounds
    rounds += 1
    work_sec = WORK_MIN * 60
    sh_br_sec = SHORT_BREAK_MIN * 60
    lng_br_sec = LONG_BREAK_MIN * 60

    if rounds % 8 == 0:
        title.config(text="Break", fg=RED, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
        countdown(lng_br_sec)
        print(rounds)
    elif rounds % 2 == 0:
        title.config(text="Break", fg=PINK, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
        countdown(sh_br_sec)
        print(rounds)
    else:
        countdown(work_sec)
        title.config(text="Work", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
        print(rounds)


def reset():
    global rounds
    window.after_cancel(timer_count)
    canvas.itemconfig(timer, text="00:00")
    check.config(text='')
    title.config(text="Timer")
    rounds = 0

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    canvas.itemconfig(timer, text=count)
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = '0' + str(count_sec)

    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_count
        timer_count = window.after(1000, countdown, count-1)
    else:
        start()
        mark = ''
        work_sesions = math.floor(rounds/2)
        for _ in range(work_sesions):
            mark += "✔"
            check.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# title label
title = Label(text="Timer")
title.config(fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
title.grid(row=1, column=2)

# Checkmark

check = Label()
check.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16))
check.grid(row=4, column=2)

# Tomato image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 113, image=tomato_png)
timer = canvas.create_text(101.75, 113, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

# Reset button

r_button = Button(text="Reset", command=reset)
r_button.grid(row=3, column=3)

# Start button

s_button = Button(text="Start", command=start)
s_button.grid(row=3, column=1)



window.mainloop()