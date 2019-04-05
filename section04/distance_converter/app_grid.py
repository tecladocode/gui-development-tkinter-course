import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Distance Converter")

feet_value = tk.StringVar()
metres_value = tk.StringVar()


def calculate_feet(*args):
    try:
        value = float(metres_value.get())
        feet_value.set('%.3f' % (value * 3.28084))
    except ValueError:
        pass


main = ttk.Frame(root, padding="30 15 30 15")
main.grid()

root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

metres_label = ttk.Label(main, text="metres")
metres_label.grid(column=0, row=0, sticky="W", padx=5, pady=5)
metres_input = ttk.Entry(main, width=10, textvariable=metres_value)
metres_input.grid(column=1, row=0, sticky="EW", padx=5, pady=5)
metres_input.focus()

feet_label = ttk.Label(main, text="feet")
feet_label.grid(column=0, row=1, sticky="W", padx=5, pady=5)
feet_display = ttk.Label(main, textvariable=feet_value)
feet_display.grid(column=1, row=1, sticky="EW", padx=5, pady=5)

calc_button = ttk.Button(main, text="Calculate", command=calculate_feet)
calc_button.grid(column=0, row=2, columnspan=2, sticky="EW", padx=5, pady=5)

root.bind("<Return>", calculate_feet)
root.bind("<KP_Enter>", calculate_feet)

root.mainloop()
