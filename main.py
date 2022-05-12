# Tkinter Imports
from tkinter import *
from tkinter import ttk

# Other imports
import time

# Countdown function
def countdown(
    win,
    hours_label,
    minutes_label,
    seconds_label,
    time_values=[0, 0, 0],
    break_time=1,
    rounds=1,
    sequence="",
    learn_time=[0, 1, 0],
    is_paused=False,
):
    h, m, s = time_values
    try:
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
            if int(rounds.get()) > 1 and sequence == "break":
                rounds.set(int(rounds.get()) - 1)
                break_timer(break_time, rounds, learn_time)
            elif int(rounds.get()) > 0 and sequence == "learn":
                learn_timer(rounds, learn_time, break_time)
        if is_paused.get() == False:
            temp -= 1


# Pausing function
def pause(btn, is_paused):
    if btn["text"] == "Start":
        btn["text"] = "Pause"
    elif btn["text"] == "Unpause":
        is_paused.set(not is_paused.get())
        btn["text"] = "Pause"
    elif btn["text"] == "Pause":
        is_paused.set(not is_paused.get())
        btn["text"] = "Unpause"


# Window in which user can set amount of rounds,learning time and break time, 1st window that user sees
def menu():
    menu = Tk()
    menu.title("Pomodoro timer")

    mainframe = ttk.Frame(menu)
    mainframe.pack(expand="True", padx=36, pady=36)
    rounds = StringVar(value=1)
    hours = StringVar(value=0)
    minutes = StringVar(value=0)
    seconds = StringVar(value=0)
    break_time = StringVar(value=1)

    rounds_label = ttk.Label(mainframe, text="Number of rounds").pack()
    rounds_entry = ttk.Entry(
        mainframe, textvariable=rounds, width=4, justify="center"
    ).pack()

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
        width=4,
        wrap=True,
        textvariable=hours,
        command=lambda: hours.set(hours.get()),
        justify="center",
    ).grid(column=0, row=2)
    minutes_entry = ttk.Spinbox(
        time_entry_frame,
        from_=0,
        to=60,
        width=4,
        wrap=True,
        textvariable=minutes,
        command=lambda: minutes.set(minutes.get()),
        justify="center",
    ).grid(column=1, row=2)
    seconds_entry = ttk.Spinbox(
        time_entry_frame,
        from_=0,
        to=60,
        width=4,
        wrap=True,
        textvariable=seconds,
        command=lambda: seconds.set(seconds.get()),
        justify="center",
    ).grid(column=2, row=2)

    break_time_label = ttk.Label(mainframe, text="Break time (minutes)").pack()
    break_time_entry = ttk.Entry(
        mainframe, textvariable=break_time, width=5, justify="center"
    ).pack()

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

    menu.mainloop()


# Window in which you see countdown and rounds left, 2nd window that user sees
def learn_timer(rounds, time, break_time):
    h, m, s = time
    timer_win = Tk()
    timer_win.title("Timer")
    mainframe = ttk.Frame(timer_win)
    mainframe.pack(expand="True", padx=36, pady=36)

    hours = StringVar(value=h)
    minutes = StringVar(value=m)
    seconds = StringVar(value=s)
    is_paused = BooleanVar(value=False)

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
        text="Start",
        command=lambda: [
            pause(pause_button, is_paused),
            countdown(
                timer_win,
                hours_label,
                minutes_label,
                seconds_label,
                [int(h), int(m), int(s)],
                break_time,
                rounds,
                "break",
                [int(h), int(m), int(s)],
                is_paused,
            ),
        ]
        if pause_button["text"] == "Start"
        else pause(pause_button, is_paused),
    )
    pause_button.grid(column=1, row=2, padx=5, pady=10)
    timer_win.mainloop()


# Window in which you see break time, 3rd window that user sees
def break_timer(break_time, rounds, learn_time):
    break_win = Tk()
    break_win.title("Break Time")
    mainframe = ttk.Frame(break_win)
    mainframe.pack(expand="True", padx=36, pady=36)

    is_paused = BooleanVar(value=False)

    main_text = ttk.Label(mainframe, text="Break Time!").pack()

    timer_frame = LabelFrame(mainframe, border=0, padx=0, pady=10)
    timer_frame.pack()
    hours_label = ttk.Label(timer_frame)  # Created because of need of argument
    minutes_text = ttk.Label(timer_frame, text="Minutes").grid(column=0, row=0, padx=5)
    seconds_text = ttk.Label(timer_frame, text="Seconds").grid(column=1, row=0, padx=5)
    minutes_label = ttk.Label(timer_frame, text=break_time)
    minutes_label.grid(column=0, row=1, padx=5)
    seconds_label = ttk.Label(timer_frame, text="0")
    seconds_label.grid(column=1, row=1, padx=5)

    pause_button = ttk.Button(
        mainframe,
        text="Start",
        command=lambda: [
            pause(pause_button, is_paused),
            countdown(
                break_win,
                hours_label,
                minutes_label,
                seconds_label,
                [0, int(break_time), 0],
                break_time,
                rounds,
                "learn",
                learn_time,
                is_paused,
            ),
        ]
        if pause_button["text"] == "Start"
        else pause(pause_button, is_paused),
    )

    pause_button.pack(pady=6)
    break_win.mainloop()


# TODO: Create Window with todo list, summary and GUI with all components working together
# TODO: Validation of user inputs
# TODO: Kill the app on exit event


if __name__ == "__main__":
    menu()
