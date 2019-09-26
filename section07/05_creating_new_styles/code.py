import tkinter as tk
from tkinter import ttk


root = tk.Tk()
style = ttk.Style(root)

# Add this after showing error happens when using non-existent style
style.configure("CustomEntryStyle.TEntry", padding=20)  # This adds an inherited style, copying everything from TEntry

name = ttk.Label(root, text="Hello, world!", style="TLabel")  # Change to CustomLabel and see error appear
entry = ttk.Entry(root, width=15)
entry["style"] = "CustomEntryStyle.TEntry"  # Change style after creation is possible too
name.pack()
entry.pack()

# Add this even later, to show the ttk.Entry hasn't changed, it's just due to the style.
entry2 = ttk.Entry(root, width=15)
entry2.pack()

root.mainloop()

