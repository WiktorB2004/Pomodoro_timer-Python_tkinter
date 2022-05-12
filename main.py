# Imports
from tkinter import *
from tkinter import ttk
import time


# Window in which you see break time
def break_timer(break_time, rounds):
    pass


# Countdown function
def countdown(
    win, hours_label, minutes_label, seconds_label, time_values, break_time, rounds
):
    h, m, s = time_values
    try:
        # the input provided by the user is
        # stored in here :temp
        temp = h * 3600 + m * 60 + s
    except:
        raise ValueError("Please input valid value")
    while temp > -1:
        mins, secs = divmod(temp, 60)
        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)

        hours_label["text"] = hours
        minutes_label["text"] = mins
        seconds_label["text"] = secs

        win.update()
        time.sleep(1)

        if temp == 0:
            win.destroy()
            rounds.set(int(rounds.get()) - 1)
            break_timer(break_time, rounds)

        temp -= 1


# Pausing button function
def pause(btn):
    if btn["text"] == "Unpause":
        btn["text"] = "Pause"
    else:
        btn["text"] = "Unpause"


# Window in which you see countdown and rounds left
def learn_timer(rounds, time, break_time):
    h, m, s = time
    timer_win = Tk()
    timer_win.title("Timer")
    mainframe = ttk.Frame(timer_win)
    mainframe.pack(expand="True", padx=36, pady=36)

    hours = StringVar(value=h)
    minutes = StringVar(value=m)
    seconds = StringVar(value=s)

    main_text = ttk.Label(mainframe, text="Counting down...").pack()
    rounds_text = ttk.Label(mainframe, text=f"Rounds left: {rounds.get()}").pack()

    timer_frame = LabelFrame(mainframe, border=0, padx=0, pady=0)
    timer_frame.pack()
    hours_text = ttk.Label(timer_frame, text="Hours")
    hours_text.grid(column=0, row=0, padx=5)
    minutes_text = ttk.Label(timer_frame, text="Minutes").grid(column=1, row=0, padx=5)
    seconds_text = ttk.Label(timer_frame, text="Seconds").grid(column=2, row=0, padx=5)
    hours_label = ttk.Label(timer_frame, text=hours.get())
    hours_label.grid(column=0, row=1, padx=5)
    minutes_label = ttk.Label(timer_frame, text=minutes.get())
    minutes_label.grid(column=1, row=1, padx=5)
    seconds_label = ttk.Label(timer_frame, text=seconds.get())
    seconds_label.grid(column=2, row=1, padx=5)
    pause_button = ttk.Button(
        timer_frame,
        text="Pause",
        command=lambda: pause(pause_button),
    )
    pause_button.grid(column=1, row=2, padx=5, pady=10)
    countdown(
        timer_win,
        hours_label,
        minutes_label,
        seconds_label,
        [int(h), int(m), int(s)],
        break_time,
        rounds,
    )
    timer_win.mainloop()


# Window in which you can set amount of rounds and learning and break time
def menu():
    menu = Tk()
    menu.title("Pomodoro timer")

    mainframe = ttk.Frame(menu)
    mainframe.pack(expand="True", padx=36, pady=36)
    rounds = StringVar(value=0)
    hours = StringVar(value=0)
    minutes = StringVar(value=0)
    seconds = StringVar(value=0)
    break_time = StringVar(value=0)

    rounds_label = ttk.Label(mainframe, text="Number of rounds").pack()
    rounds_entry = ttk.Entry(mainframe, textvariable=rounds, width="5").pack()

    time_entry_frame = LabelFrame(mainframe, border=0, padx=10, pady=10)
    time_entry_frame.pack()
    time_label = ttk.Label(time_entry_frame, text="Learning time").grid(column=1, row=0)
    hours_label = ttk.Label(time_entry_frame, text="hours").grid(column=0, row=1)
    minutes_label = ttk.Label(time_entry_frame, text="minutes").grid(column=1, row=1)
    seconds_label = ttk.Label(time_entry_frame, text="seconds").grid(column=2, row=1)
    hours_entry = ttk.Spinbox(
        time_entry_frame,
        from_=0,
        to=60,
        width=5,
        wrap=True,
        textvariable=hours,
        command=lambda: hours.set(hours.get()),
    ).grid(column=0, row=2)
    minutes_entry = ttk.Spinbox(
        time_entry_frame,
        from_=0,
        to=60,
        width=5,
        wrap=True,
        textvariable=minutes,
        command=lambda: minutes.set(minutes.get()),
    ).grid(column=1, row=2)
    seconds_entry = ttk.Spinbox(
        time_entry_frame,
        from_=0,
        to=60,
        width=5,
        wrap=True,
        textvariable=seconds,
        command=lambda: seconds.set(seconds.get()),
    ).grid(column=2, row=2)

    break_time_label = ttk.Label(mainframe, text="Break time").pack()
    break_time_entry = ttk.Entry(mainframe, textvariable=break_time, width=5).pack()

    submit_button = ttk.Button(
        mainframe,
        text="Start",
        command=lambda: [
            menu.destroy(),
            learn_timer(
                rounds,
                [hours.get(), minutes.get(), seconds.get()],
                break_time.get(),
            ),
        ],
    ).pack(pady=15)
    mainloop()


# TODO: Create Window with todo list, summary and GUI with all components working together

if __name__ == "__main__":
    menu()
