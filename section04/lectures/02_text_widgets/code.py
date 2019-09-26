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
root.resizable(False, False)
root.title("Widget Examples")

# -- Text widgets --

# height is the number of rows of text
text = tk.Text(root, height=8)  # Show what happens if you `.pack()` here, while still assigning to variable.
text.pack()

# Insert content into the text area
text.insert("1.0", "Please enter a comment...")  # Can use \n to insert multiple lines.

# First argument: position within textarea.
# Second argument: text to insert after that position.

# The position is given as two numbers, separated by a `.`.
# First number is the line number, starting at 1.
# Second number is character number within the line, starting at 0.
# So 1.0 is the first line, first character.

# -- Disable text widget --

text["state"] = "disabled"  # "normal" is the counterpart

# -- Get text content --

text_content = text.get("1.0", "end")
print(text_content)

root.mainloop()