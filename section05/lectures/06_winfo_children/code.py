import tkinter as tk
import tkinter.font as font
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

root = tk.Tk()
root.title("Distance Converter")

font.nametofont("TkDefaultFont").configure(size=15)

feet_value = tk.StringVar()
metres_value = tk.StringVar()


def calculate_feet(*args):
    try:
        metres = float(metres_value.get())
        feet = metres * 3.28084
        feet_value.set(f"{feet:.3f}")
    except ValueError:
        pass


main = ttk.Frame(root, padding=(60, 30))
main.grid()

root.columnconfigure(0, weight=1)

# -- Widgets --

metres_label = ttk.Label(main, text="metres")
metres_input = ttk.Entry(main, width=10, textvariable=metres_value, font=(None, 15))  # None means "don't change the font".
feet_label = ttk.Label(main, text="feet")
feet_display = ttk.Label(main, textvariable=feet_value)
calc_button = ttk.Button(main, text="Calculate", command=calculate_feet)

# -- Layout --

metres_label.grid(column=0, row=0, sticky="W")
metres_input.grid(column=1, row=0, sticky="EW")
metres_input.focus()

feet_label.grid(column=0, row=1, sticky="W")
feet_display.grid(column=1, row=1, sticky="EW")

calc_button.grid(column=0, row=2, columnspan=2, sticky="EW")


# winfo_children stands for "widget info children", and gets all the children of a widget.
for child in main.winfo_children():
    child.grid_configure(padx=15, pady=15)


root.bind("<Return>", calculate_feet)
root.bind("<KP_Enter>", calculate_feet)

root.mainloop()