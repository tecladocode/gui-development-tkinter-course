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

# Like labels, here we can use images or compounds of images and text.
check_button = ttk.Checkbutton(root, text="Check me!")
check_button.pack()

check_button["state"] = "disabled"  # "normal" is the counterpart


# -- All options --

selected_option = tk.StringVar()

def print_current_option():
    print(selected_option.get())

check = tk.Checkbutton(
    root,
    text="Check Example",
    variable=selected_option,
    command=print_current_option,
    onvalue="On",
    offvalue="Off"
)

check.pack()


root.mainloop()