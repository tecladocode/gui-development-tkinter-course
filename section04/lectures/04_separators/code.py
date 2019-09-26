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

label = ttk.Label(root, text="Hello, World!", padding=20)
# label.config(font=("Segoe UI", 20))
label.pack()

main_sep = ttk.Separator(root, orient="horizontal")
main_sep.pack(fill="x")  # Remove fill, what happens?

label = ttk.Label(root, text="Hello, World!", padding=20)
# label.config(font=("Segoe UI", 20))
label.pack()

root.mainloop()