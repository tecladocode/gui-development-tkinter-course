import tkinter as tk
from tkinter import ttk


root = tk.Tk()
style = ttk.Style(root)

name = ttk.Label(root, text="Hello, world!")
entry = ttk.Entry(root, width=15)
name.pack()

print(name.winfo_class())
print(entry.winfo_class())  # No need to place in window to get style class

root.mainloop()

