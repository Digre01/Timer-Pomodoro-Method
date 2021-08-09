# Pomodoro Method Timer by Digre
# this app will help you to study, is setted for session of 25 minutes and 5 for pauses (after 4 pauses there will be one of 15 minutes)

import tkinter as tk
import time
from tkinter import *
from tkinter import messagebox

stop = False
pause = False
timer_pause = False
temp = 0
sequence = 0

window = tk.Tk()
window.geometry("400x300")
window.title("Pomodoro Timer")
window.iconbitmap("../pomodoro.ico")
window.grid_columnconfigure(0, weight=1)
window.resizable(False, False)

welcome_label = tk.Label(window,
                         text="Welcome! insert the number of the study sessions",
                         font=("Helvetica", 12))
welcome_label.grid(row=0, column=0, sticky="N", padx=20, pady=10)

minute = StringVar()
second = StringVar()
message = StringVar()

minute.set("00")
second.set("00")
message.set("Are you ready?")

number_input = tk.Entry(width=10)
number_input.grid(row=1, column=0)

minuteEntry = Entry(width=2, font=("Arial", 32, ""),
                    textvariable=minute).place(x=130, y=150)

secondEntry = Entry(width=2, font=("Arial", 32, ""),
                    textvariable=second).place(x=215, y=150)

text_input = Entry(width=40, font=("Arial", 11, ""),
                   textvariable=message).place(x=35, y=220)


def timer():
    global stop, minute, second, temp, timer_pause, pause

    ripetizioni = number_input.get()
    if not ripetizioni.isdigit():
        stop = True
    else:
        stop = False

    sequence = int(ripetizioni)
    count = 0
    while (sequence > count) & (stop == False):
        pause = False
        count += 1

        if not timer_pause:
            temp = 25 * 60
        else:
            temp = temp_paused

        timer_pause = False

        while temp > -1:

            if not stop:

                mins, secs = divmod(temp, 60)
                messagechange(pause)

                minute.set("{0:2d}".format(mins))
                second.set("{0:2d}".format(secs))

                window.update()
                time.sleep(1)
                temp -= 1

                if temp == 0 & pause == False & stop == False:
                    pause = True
                    alert(pause)
                    messagechange(pause)
                    window.update()

                    if count % 4 == 0:
                        temp = 15 * 60
                    else:
                        temp = 5 * 60

                    while temp > -1:
                        mins, secs = divmod(temp, 60)
                        minute.set("{0:2d}".format(mins))
                        second.set("{0:2d}".format(secs))

                        window.update()
                        time.sleep(1)

                        temp -= 1
                    pause = False
                    print("pausa")
                    if sequence != count:
                        alert(pause)
                        messagechange(pause)

                if temp == 0:
                    alert(pause)
                    messagechange(pause)

            else:
                break

    else:
        if not timer_pause:
            message.set("ok Let's Start, Give me an int number")
            window.update()
        else:
            message.set("Timer Stopped")
            window.update()

    if timer_pause == False & stop == False:
        messagebox.showinfo(title='Pomodoro Alert', message='CONGRATULATION! you have finished your daily studies')


def stop_timer():
    global stop, minute, second, flag
    stop = True
    minute.set("00")
    second.set("00")
    window.update()


def pause_timer():
    global stop, minute, second, flag, timer_pause, temp_paused

    if stop:
        stop = False
        timer_pause = False
    else:
        stop = True
        timer_pause = True

    temp_paused = temp


def alert(pause):
    if pause:
        messagebox.showinfo(title='Pomodoro Alert', message='Take a Break')
    else:
        messagebox.showinfo(title='Pomodoro Alert', message='Lets continue our studies!')


def messagechange(pause):
    if pause:
        message.set("PAUSE, you should relax and take a coffee")
    if not pause:
        message.set("STUDY TIME, put your phone away!")


start_button = tk.Button(text="Start!", command=timer).place(x=180, y=80)

pause_button = tk.Button(text="Pause", command=pause_timer).place(x=110, y=80)

reset_button = tk.Button(text="Reset", command=stop_timer).place(x=250, y=80)

if __name__ == "__main__":
    window.mainloop()
