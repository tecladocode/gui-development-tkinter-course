import tkinter as tk
from tkinter import ttk

# -- Windows only configuration --
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
# -- End Windows only configuration --

root = tk.Tk()
root.title("Widget Examples")


initial_value = tk.StringVar(value=20)
spin_box = tk.Spinbox(
    root,
    from_=0,
    to=30,
    textvariable=initial_value,
    wrap=False)
# spin_box = tk.Spinbox(root, values=(5, 10, 15, 20, 25, 30), textvariable=initial_value, wrap=False)
# The alternative uses values instead of a range.

spin_box.pack()

print(spin_box.get())  # You'd usually use this when clicking a button (e.g. to submit)
# Can't call `.get()` after the mainloop finishes, of course.

root.mainloop()
