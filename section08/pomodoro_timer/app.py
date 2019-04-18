from tkinter import ttk
import tkinter as tk

class PomodoroTimer(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Pomodoro Timer")

        container = ttk.Frame(self)
        container.grid(padx=10, pady=10, sticky="EW")
        
        self.pomodoro = tk.StringVar(value=25)
        self.long_break = tk.StringVar(value=10)
        self.short_break = tk.StringVar(value=5)

        self.frames = {}

        for F in (Home, Settings, Timer):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="NESW")

        self.show_frame(Home)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


class Home(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # TODO: Create the home interface with three buttons: start, quit, and settings. Setting will likely have an icon.

        start_button = ttk.Button(self, text="Start")
        settings_button = ttk.Button(self, text="Settings", command=lambda: controller.show_frame(Settings)).pack()


class Settings(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        settings_container = ttk.Frame(self, padding="30 15 30 15")
        settings_container.grid()

        pomodoro_label = ttk.Label(settings_container, text="Pomodoro: ")
        pomodoro_label.grid(column=0, row=0, sticky="W")
        pomodoro_input = tk.Spinbox(
            settings_container,
            from_=0,
            to=120,
            increment=1,
            justify="center",
            textvariable=controller.pomodoro,
            width=10
        )
        pomodoro_input.grid(column=1, row=0, sticky="EW")
        pomodoro_input.focus()

        long_break_label = ttk.Label(settings_container, text="Long break time: ")
        long_break_label.grid(column=0, row=1, sticky="W")
        long_break_input = tk.Spinbox(
            settings_container,
            from_=0,
            to=60,
            increment=1,
            justify="center",
            textvariable=controller.long_break,
            width=10
        )
        long_break_input.grid(column=1, row=1, sticky="EW")

        short_break_label = ttk.Label(settings_container, text="Short break time: ")
        short_break_label.grid(column=0, row=2, sticky="W")
        short_break_input = tk.Spinbox(
            settings_container,
            from_=0,
            to=30,
            increment=1,
            justify="center",
            textvariable=controller.short_break,
            width=10
        )
        short_break_input.grid(column=1, row=2, sticky="EW")

        for child in settings_container.winfo_children():
            child.grid_configure(padx=5, pady=5)


class Timer(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

    # TODO: Create a timer area with custom styling to display the remaining time. Add four buttons to control the timer and access the settings panel.


root = PomodoroTimer()
root.mainloop()
