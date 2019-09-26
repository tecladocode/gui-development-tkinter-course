import tkinter as tk
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

root = tk.Tk()
root.title("Distance Converter")

metres_value = tk.StringVar()

def calculate_feet(*args):
    try:
        metres = float(metres_value.get())
        feet = metres * 3.28084
        print(f"{metres} metres is equal to {feet:.3f} feet.")
    except ValueError:
        pass


main = ttk.Frame(root, padding=(30, 15))
main.grid()

root.columnconfigure(0, weight=1)

# -- Widgets --

metres_label = ttk.Label(main, text="metres")
metres_input = ttk.Entry(main, width=10, textvariable=metres_value)
feet_label = ttk.Label(main, text="feet")
feet_display = ttk.Label(main, text="Feet shown here")
calc_button = ttk.Button(main, text="Calculate", command=calculate_feet)

# -- Layout --

metres_label.grid(column=0, row=0, sticky="W", padx=5, pady=5)
metres_input.grid(column=1, row=0, sticky="EW", padx=5, pady=5)
metres_input.focus()

feet_label.grid(column=0, row=1, sticky="W", padx=5, pady=5)
feet_display.grid(column=1, row=1, sticky="EW", padx=5, pady=5)

calc_button.grid(column=0, row=2, columnspan=2, sticky="EW", padx=5, pady=5)

root.mainloop()