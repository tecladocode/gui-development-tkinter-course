import tkinter as tk
from tkinter import ttk

# TODO: Get bindings to work inside the classes.


class DistanceConverter(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Distance Calculator")

        container = ttk.Frame(self)
        container.grid(padx=10, pady=10, sticky=("E", "W"))

        self.frames = {}

        for F in (MetresToFeet, FeetToMetres):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=("N", "S", "E", "W"))

        self.show_frame(MetresToFeet)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


class MetresToFeet(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.feet_value = tk.StringVar()
        self.metres_value = tk.StringVar()

        metres_label = ttk.Label(self, text="metres")
        metres_label.grid(column=1, row=1, sticky="W", ipadx=5)

        feet_label = ttk.Label(self, text="feet")
        feet_label.grid(column=1, row=2, sticky="W", ipadx=5)

        metres_input = ttk.Entry(
            self, width=10, textvariable=self.metres_value)
        metres_input.grid(column=2, row=1, sticky=("E", "W"))

        feet_display = ttk.Label(self, textvariable=self.feet_value)
        feet_display.grid(column=2, row=2, sticky=("E", "W"))

        calculate_button = ttk.Button(
            self, text="Calculate", command=self.calculate_feet)
        calculate_button.grid(column=1, row=3, columnspan=2, sticky=("E", "W"))

        switch_page_button = ttk.Button(
            self, text="Switch to feet conversion", command=lambda: controller.show_frame(FeetToMetres))
        switch_page_button.grid(
            column=1, row=4, columnspan=2, sticky=("E", "W"))

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

        metres_input.focus()

    def calculate_feet(self, *args):
        try:
            value = float(self.metres_value.get())
            self.feet_value.set('%.3f' % (value * 3.28084))
        except ValueError:
            pass


class FeetToMetres(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.feet_value = tk.StringVar()
        self.metres_value = tk.StringVar()

        feet_label = ttk.Label(self, text="feet")
        feet_label.grid(column=1, row=1, sticky="W", ipadx=5)

        metres_label = ttk.Label(self, text="metres")
        metres_label.grid(column=1, row=2, sticky="W", ipadx=5)

        feet_input = ttk.Entry(self, width=10, textvariable=self.feet_value)
        feet_input.grid(column=2, row=1, sticky=("E", "W"))

        metres_display = ttk.Label(self, textvariable=self.metres_value)
        metres_display.grid(column=2, row=2, sticky=("E", "W"))

        calculate_button = ttk.Button(
            self, text="Calculate", command=self.calculate_metres)
        calculate_button.grid(column=1, row=3, columnspan=2, sticky=("E", "W"))

        switch_page_button = ttk.Button(
            self, text="Switch to metres conversion", command=lambda: controller.show_frame(MetresToFeet))
        switch_page_button.grid(
            column=1, row=4, columnspan=2, sticky=("E", "W"))

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

        feet_input.focus()

    def calculate_metres(self, *args):
        try:
            value = float(self.feet_value.get())
            self.metres_value.set('%.3f' % (value / 3.28084))
        except ValueError:
            pass


root = DistanceConverter()
root.mainloop()
