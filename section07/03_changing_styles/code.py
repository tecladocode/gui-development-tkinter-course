import tkinter as tk
from tkinter import ttk


root = tk.Tk()
style = ttk.Style(root)

name = ttk.Label(root, text="Hello, world!", style="TLabel")  # Change to CustomLabel and see error appear
entry = ttk.Entry(root, width=15)
# entry["style"] = "CustomBtnStyle"  # Change style after creation is possible too
name.pack()

# This is how to change a property of the style.
# What can we change? Next video will tell us...
style.configure("TLabel", font=("Segoe UI", 20))

root.mainloop()

