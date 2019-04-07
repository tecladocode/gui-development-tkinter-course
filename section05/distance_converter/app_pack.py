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
main.pack()

metres_section = ttk.Frame(main)
metres_section.pack(fill="both")

metres_label = ttk.Label(metres_section, text="metres")
metres_label.pack(side="left", padx=5, pady=5)
metres_input = ttk.Entry(metres_section, width=10, textvariable=metres_value)
metres_input.pack(side="left", padx=5, pady=5)
metres_input.focus()

feet_section = ttk.Frame(main)
feet_section.pack(fill="both")

feet_label = ttk.Label(feet_section, text="feet")
feet_label.pack(side="left", padx=5, pady=5)
feet_display = ttk.Label(feet_section, textvariable=feet_value)
feet_display.pack(side="left", padx=5, pady=5)

calc_button = ttk.Button(main, text="Calculate", command=calculate_feet)
calc_button.pack(padx=5, pady=5, expand=True, fill="both")

root.bind("<Return>", calculate_feet)
root.bind("<KP_Enter>", calculate_feet)

root.mainloop()
