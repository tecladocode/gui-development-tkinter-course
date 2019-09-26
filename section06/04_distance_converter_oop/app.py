import tkinter as tk
from tkinter import ttk


class DistanceConverter(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Distance Converter")

        frame = MetresToFeet(self)
        frame.grid(row=0, column=0, sticky="NSEW")


class MetresToFeet(ttk.Frame):

    def __init__(self, container):
        super().__init__(container)

        self.feet_value = tk.StringVar()
        self.metres_value = tk.StringVar()

        metres_label = ttk.Label(self, text="Metres:")
        metres_label.grid(column=1, row=1, sticky="W", ipadx=5)
        metres_input = ttk.Entry(self, width=10, textvariable=self.metres_value)
        metres_input.grid(column=2, row=1, sticky="EW")
        metres_input.focus()

        feet_label = ttk.Label(self, text="Feet:")
        feet_label.grid(column=1, row=2, sticky="W", ipadx=5)
        feet_display = ttk.Label(self, textvariable=self.feet_value)
        feet_display.grid(column=2, row=2, sticky="EW")

        calculate_button = ttk.Button(
            self,
            text="Calculate",
            command=self.calculate_feet
        )
        calculate_button.grid(column=1, row=3, columnspan=2, sticky="EW")

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def calculate_feet(self, *args):
        try:
            value = float(self.metres_value.get())
            self.feet_value.set('%.3f' % (value * 3.28084))
        except ValueError:
            pass


root = DistanceConverter()
root.mainloop()
