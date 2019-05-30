from tkinter import ttk
from components.settings import Settings
from components.timer import Timer


class Home(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)

        button_container = ttk.Frame(self, padding="30 15 30 15")
        button_container.grid(row=0, column=0, sticky="EW")
        button_container.columnconfigure(0, weight=1)

        start_button = ttk.Button(
            button_container, text="Start", command=lambda: controller.show_frame(Timer)
        )
        start_button.grid(row=0, column=0, sticky="EW", pady=(0, 5))

        settings_button = ttk.Button(
            button_container,
            text="Settings",
            command=lambda: controller.show_frame(Settings),
        )
        settings_button.grid(row=1, column=0, sticky="EW", pady=(0, 5))

        quit_button = ttk.Button(
            button_container, text="Quit", command=controller.destroy
        )
        quit_button.grid(row=2, column=0, sticky="EW")
