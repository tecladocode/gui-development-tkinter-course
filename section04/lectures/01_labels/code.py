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

# -- Label as text, as we've seen --

label = ttk.Label(root, text="Hello, World!", padding=20)
label.config(font=("Segoe UI", 20))  # Could be in the constructor instead.
label.pack()


# -- Labels with images --

from PIL import Image, ImageTk  # Need to pip install Pillow

# Need an image in the folder you run the file from, called "test_image.png"
image = Image.open("test_image.png") #.resize((64, 64))
photo = ImageTk.PhotoImage(image)
ttk.Label(root, image=photo, padding=5).pack()

# This is how you change an image associated with a label, if necessary:
# label["image"] = photo


# -- Changing the text of a label dynamically --

greeting = tk.StringVar()

label = ttk.Label(root, padding=10)
label["textvariable"] = greeting
greeting.set("Hello, John!")  # This can change during your program and the label will update.
label.pack()


# -- Combining text and images --

text_image = Image.open("test_image.png")
text_photo = ImageTk.PhotoImage(text_image)
ttk.Label(root, text="Image with text.", image=text_photo, padding=5, compound="right").pack()

root.mainloop()