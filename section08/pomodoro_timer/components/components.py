import tkinter as tk
from tkinter import ttk
from collections import deque


class Settings(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self["style"] = "Background.TFrame"

        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        self.settings_container = ttk.Frame(
            self,
            padding="30 15 30 15",
            style="Background.TFrame"
        )
        self.settings_container.grid(row=0, column=0, sticky="EW", padx=10, pady=10)

        self.settings_container.columnconfigure(0, weight=1)
        self.settings_container.rowconfigure(1, weight=1)

        self.pomodoro_label = ttk.Label(
            self.settings_container,
            text="Pomodoro: ",
            style="LightText.TLabel"
        )
        self.pomodoro_label.grid(column=0, row=0, sticky="W")
        self.pomodoro_input = tk.Spinbox(
            self.settings_container,
            from_=0,
            to=120,
            increment=1,
            justify="center",
            textvariable=controller.pomodoro,
            width=10,
        )
        self.pomodoro_input.grid(column=1, row=0, sticky="EW")
        self.pomodoro_input.focus()

        self.long_break_label = ttk.Label(
            self.settings_container,
            text="Long break time: ",
            style="LightText.TLabel"
        )
        self.long_break_label.grid(column=0, row=1, sticky="W")
        self.long_break_input = tk.Spinbox(
            self.settings_container,
            from_=0,
            to=60,
            increment=1,
            justify="center",
            textvariable=controller.long_break,
            width=10,
        )
        self.long_break_input.grid(column=1, row=1, sticky="EW")

        self.short_break_label = ttk.Label(
            self.settings_container,
            text="Short break time: ",
            style="LightText.TLabel"
        )
        self.short_break_label.grid(column=0, row=2, sticky="W")
        self.short_break_input = tk.Spinbox(
            self.settings_container,
            from_=0,
            to=30,
            increment=1,
            justify="center",
            textvariable=controller.short_break,
            width=10,
        )
        self.short_break_input.grid(column=1, row=2, sticky="EW")

        for child in self.settings_container.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.button_container = ttk.Frame(self, style="Background.TFrame")
        self.button_container.grid(sticky="EW", padx=10)
        self.button_container.columnconfigure(0, weight=1)

        self.timer_button = ttk.Button(
            self.button_container,
            text="← Back",
            command=lambda: controller.show_frame(Timer),
            style="PomodoroButton.TButton"
        )
        self.timer_button.grid(column=0, row=0, sticky="EW", padx=2
        )


class Timer(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self["style"] = "Background.TFrame"

        self.controller = controller
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)

        self.current_timer = tk.StringVar(value=controller.timer_schedule[0])

        self.settings_button = ttk.Button(
            self,
            text="Settings",
            command=lambda: controller.show_frame(Settings),
            style="PomodoroButton.TButton"
        )
        self.settings_button.grid(row=0, column=1, sticky="E", padx=10, pady=(10, 0))

        self.timer_description = ttk.Label(
            self,
            textvariable=self.current_timer,
            style="LightText.TLabel"
        )
        self.timer_description.grid(row=0, column=0, sticky="W", padx=(10, 0), pady=(10, 0))

        self.timer_frame = ttk.Frame(self, height="100", style="Timer.TFrame")
        self.timer_frame.grid(row=1, column=0, columnspan=2, pady=(10, 0), sticky="NSEW")

        self.timer_counter = ttk.Label(
            self.timer_frame,
            textvariable=controller.current_time,
            style="TimerText.TLabel"
        )
        self.timer_counter.place(relx=.5, rely=.5, anchor="center")

        self.button_container = ttk.Frame(self, padding=10, style="Background.TFrame")
        self.button_container.grid(row=2, column=0, columnspan=2, sticky="EW")
        self.button_container.columnconfigure((0, 1, 2), weight=1)

        self.start_button = ttk.Button(
            self.button_container,
            text="Start",
            command=self.start_timer,
            style="PomodoroButton.TButton"
        )
        self.start_button.grid(row=0, column=0, sticky="EW")

        self.stop_button = ttk.Button(
            self.button_container,
            text="Stop",
            state="disabled",
            command=self.stop_timer,
            style="PomodoroButton.TButton"
        )
        self.stop_button.grid(row=0, column=1, sticky="EW", padx=5)

        self.reset_button = ttk.Button(
            self.button_container,
            text="Reset",
            command=self.reset_timer,
            style="PomodoroButton.TButton"
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
