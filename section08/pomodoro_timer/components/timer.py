import tkinter as tk
from tkinter import ttk
from components.settings import Settings
from collections import deque


class Timer(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)

        self.current_timer = tk.StringVar(value=controller.timer_schedule[0])

        style = ttk.Style()
        style.configure("Timer.TFrame", background="black")
        style.configure(
            "TimerText.TLabel",
            background="black",
            foreground="red",
            font="Courier 38"
        )

        # TODO: Create a timer area with custom styling to display the remaining time. Add four buttons to control the timer and access the settings panel.

        self.settings_button = ttk.Button(
            self, text="Settings", command=lambda: controller.show_frame(Settings)
        )
        self.settings_button.grid(row=0, column=1, sticky="E", padx=10)

        self.timer_description = ttk.Label(self, textvariable=self.current_timer)
        self.timer_description.grid(row=0, column=0, sticky="W", padx=(10, 0))

        self.timer_frame = ttk.Frame(self, height="100", style="Timer.TFrame")
        self.timer_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=(10, 0), sticky="NSEW")

        self.timer_counter = ttk.Label(
            self.timer_frame,
            textvariable=controller.current_time,
            style="TimerText.TLabel"
        )
        self.timer_counter.place(relx=.5, rely=.5, anchor="center")

        self.button_container = ttk.Frame(self, padding=10)
        self.button_container.grid(row=2, column=0, columnspan=2, sticky="EW")
        self.button_container.columnconfigure((0, 1, 2), weight=1)

        self.start_button = ttk.Button(
            self.button_container,
            text="Start",
            command=self.start_timer
        )
        self.start_button.grid(row=0, column=0, sticky="EW")

        self.stop_button = ttk.Button(
            self.button_container,
            text="Stop",
            state="disabled",
            command=self.stop_timer
        )
        self.stop_button.grid(row=0, column=1, sticky="EW", padx=5)

        self.reset_button = ttk.Button(
            self.button_container,
            text="Reset",
            command=self.reset_timer
        )
        self.reset_button.grid(row=0, column=2, sticky="EW")

    def start_timer(self):
        self.controller.timer_running = True
        self.start_button["state"]= "disabled"
        self.stop_button["state"]= "enabled"
        self.decrement_time()

    def stop_timer(self):
        self.controller.timer_running = False
        self.start_button["state"]= "enabled"
        self.stop_button["state"]= "disabled"

    def reset_timer(self):
        self.stop_timer()
        pomodoro_time = self.controller.pomodoro.get()
        current_time = self.controller.current_time.set(f"{int(pomodoro_time):02d}:00")
        self.controller.timer_schedule = deque(self.controller.timer_order)
        self.current_timer.set(self.controller.timer_schedule[0])

    def decrement_time(self):
        timer_running = self.controller.timer_running
        current_time = self.controller.current_time.get()

        if timer_running and current_time != "00:00":            
            minutes, seconds = current_time.split(":")

            if int(seconds) > 0:
                seconds = int(seconds) - 1
                minutes = int(minutes)

            else:
                seconds = 59
                minutes = int(minutes) - 1

            self.controller.current_time.set(f"{minutes:02d}:{seconds:02d}")
            self.after(1000, self.decrement_time)

        elif timer_running and current_time == "00:00":
            self.controller.timer_schedule.rotate(-1)
            next_up = self.controller.timer_schedule[0]

            if next_up == "Pomodoro":
                pomodoro_time = int(self.controller.pomodoro.get())
                self.controller.current_time.set(f"{pomodoro_time:02d}:00")

            elif next_up == "Short Break":
                short_break_time = int(self.controller.short_break.get())
                self.controller.current_time.set(f"{short_break_time:02d}:00")

            elif next_up == "Long Break":
                long_break_time = int(self.controller.long_break.get())
                self.controller.current_time.set(f"{long_break_time:02d}:00")
            
            self.current_timer.set(next_up)
            self.after(1000, self.decrement_time)
        else:
            return
