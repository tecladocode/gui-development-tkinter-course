import tkinter as tk
from tkinter import ttk
from collections import deque
from frames import Timer, Settings


class PomodoroTimer(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Pomodoro Timer")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.pomodoro = tk.StringVar(value=25)
        self.long_break = tk.StringVar(value=15)
        self.short_break = tk.StringVar(value=5)
        self.timer_order = ["Pomodoro", "Short Break", "Pomodoro", "Short Break", "Pomodoro", "Long Break"]
        self.timer_schedule = deque(self.timer_order)

        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)

        self.frames = {}

        settings_frame = Settings(container, self, lambda: self.show_frame(Timer))
        timer_frame = Timer(container, self, lambda: self.show_frame(Settings))
        settings_frame.grid(row=0, column=0, sticky="NESW")
        timer_frame.grid(row=0, column=0, sticky="NESW")

        self.frames[Settings] = settings_frame
        self.frames[Timer] = timer_frame
        
        self.show_frame(Timer)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

app = PomodoroTimer()
app.mainloop()