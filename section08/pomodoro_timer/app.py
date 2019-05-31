from tkinter import ttk
import tkinter as tk
from components.components import Home, Settings, Timer
from collections import deque

COLOUR_PRIMARY = "#360568"
COLOR_PRIMARY_DARK = "#31045E"
COLOUR_SECONDARY = "#6B42B2"
COLOUR_LIGHT_TEXT = "#EBE0FF"


class PomodoroTimer(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        style = ttk.Style()
        style.configure("Timer.TFrame", background=COLOUR_PRIMARY)
        style.configure("Background.TFrame", background=COLOUR_PRIMARY)
        style.configure(
            "TimerText.TLabel",
            background=COLOUR_PRIMARY,
            foreground=COLOUR_SECONDARY,
            font="Courier 38"
        )
        style.configure(
            "LightText.TLabel",
            background=COLOUR_PRIMARY,
            foreground=COLOUR_LIGHT_TEXT,
            font="9"
        )
        style.configure(
            "PomodoroButton.TButton",
            background=COLOR_PRIMARY_DARK,
            foreground=COLOUR_LIGHT_TEXT,
            font="9"
        )
        
        # Main app window is a tk widget, so background is set directly
        self["background"] = COLOUR_PRIMARY

        self.title("Pomodoro Timer")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)

        self.pomodoro = tk.StringVar(value=25)
        self.long_break = tk.StringVar(value=15)
        self.short_break = tk.StringVar(value=5)
        self.timer_order = ["Pomodoro", "Short Break", "Pomodoro", "Short Break", "Pomodoro", "Long Break"]
        self.timer_schedule = deque(self.timer_order)
        
        self.current_time = tk.StringVar(value=f"{self.pomodoro.get()}:00")
        self.timer_running = False

        self.frames = {}

        for F in (Home, Settings, Timer):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="NESW")

        self.show_frame(Home)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


root = PomodoroTimer()
root.mainloop()
