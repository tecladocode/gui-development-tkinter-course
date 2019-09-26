import tkinter as tk
from tkinter import ttk


root = tk.Tk()
style = ttk.Style(root)

name = ttk.Label(root, text="Hello, world!")
name.pack()

# This tells us the elements within a widget
print(style.layout("TLabel"))

# This tells us the modifiable properties of each element.
# Something _really_ important is that these can be different per-theme.
print(style.element_options("Label.border"))
print(style.element_options("Label.padding"))
print(style.element_options("Label.label"))

# This tells us the current value of a property
print(style.lookup("TLabel", "font"))
print(style.lookup("TLabel", "foreground"))
print(style.lookup("TLabel", "compound"))  # Can be empty if not set


style.theme_use("clam")

# This tells us the modifiable properties of each element.
# Something _really_ important is that these can be different per-theme.
print(style.element_options("Label.border"))
print(style.element_options("Label.padding"))
print(style.element_options("Label.label"))

# This tells us the current value of a property
print(style.lookup("TLabel", "font"))
print(style.lookup("TLabel", "foreground"))
print(style.lookup("TLabel", "compound"))  # Can be empty if not set

style.configure("TLabel", bordercolor="#f00")
style.configure("TLabel", borderwidth=40)
style.configure("TLabel", relief="solid")
# More info: https://stackoverflow.com/a/39416145/1587271

root.mainloop()

