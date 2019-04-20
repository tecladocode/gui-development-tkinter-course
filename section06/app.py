import tkinter as tk
from tkinter import ttk


class DistanceConverter(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Distance Calculator")
        self.frames = {}
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        container = ttk.Frame(self)
        container.grid(padx=10, pady=10)
        container.columnconfigure(0, weight=1)

        for F in (MetresToFeet, FeetToMetres):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="NSEW")

        self.show_frame(MetresToFeet)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


class MetresToFeet(ttk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        self.feet_value = tk.StringVar()
        self.metres_value = tk.StringVar()
        self.columnconfigure((0, 1), weight=1)

        metres_label = ttk.Label(self, text="metres")
        metres_label.grid(column=0, row=0, sticky="W", ipadx=5)
        metres_input = ttk.Entry(self, width=10, textvariable=self.metres_value)
        metres_input.grid(column=1, row=0, sticky="EW")
        metres_input.focus()

        feet_label = ttk.Label(self, text="feet")
        feet_label.grid(column=0, row=1, sticky="W", ipadx=5)
        feet_display = ttk.Label(self, textvariable=self.feet_value)
        feet_display.grid(column=1, row=1, sticky="EW")

        calculate_button = ttk.Button(
            self,
            text="Calculate",
            command=self.calculate_feet
        )
        calculate_button.grid(column=0, row=2, columnspan=2, sticky="EW")

        switch_page_button = ttk.Button(
            self,
            text="Switch to feet conversion",
            command=lambda: controller.show_frame(FeetToMetres)
        )
        switch_page_button.grid(column=0, row=3, columnspan=2, sticky="EW")

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def calculate_feet(self, *args):
        try:
            value = float(self.metres_value.get())
            self.feet_value.set('%.3f' % (value * 3.28084))
        except ValueError:
            pass


class FeetToMetres(ttk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        self.feet_value = tk.StringVar()
        self.metres_value = tk.StringVar()
        self.columnconfigure((0, 1), weight=1)

        feet_label = ttk.Label(self, text="feet")
        feet_label.grid(column=1, row=1, sticky="W", ipadx=5)
        feet_input = ttk.Entry(self, width=10, textvariable=self.feet_value)
        feet_input.grid(column=2, row=1, sticky="EW")
        feet_input.focus()

        metres_label = ttk.Label(self, text="metres")
        metres_label.grid(column=1, row=2, sticky="W", ipadx=5)
        metres_display = ttk.Label(self, textvariable=self.metres_value)
        metres_display.grid(column=2, row=2, sticky="EW")

        calculate_button = ttk.Button(
            self,
            text="Calculate",
            command=self.calculate_metres
        )
        calculate_button.grid(column=1, row=3, columnspan=2, sticky="EW")

        switch_page_button = ttk.Button(
            self,
            text="Switch to metres conversion",
            command=lambda: controller.show_frame(MetresToFeet)
        )
        switch_page_button.grid(column=1, row=4, columnspan=2, sticky="EW")

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def calculate_metres(self, *args):
        try:
            value = float(self.feet_value.get())
            self.metres_value.set('%.3f' % (value / 3.28084))
        except ValueError:
            pass


root = DistanceConverter()
root.mainloop()
