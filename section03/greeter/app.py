import tkinter as tk
from tkinter import ttk

def greet():
    # The get() method is used to fetch the value of a StringVar() instance.
    print(f"Hello, {user_name.get() or 'World'}!")  # If user_name is empty, print Hello, World!

root = tk.Tk()
root.title("Greeter")

# Here we create an instances of the StringVar() class, which is to track the content of widgets
user_name = tk.StringVar()

# We define two frames to keep the input on different lines. In the next version we will switch to grid() geometry.
input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))  # Padding accepts a tuple of up to four values. Clockwise like CSS.
input_frame.pack(fill="both")
ttk.Label(input_frame, text="Name: ").pack(side="left")
name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name).pack(side="left")

buttons = ttk.Frame(root, padding=(20, 10))
buttons.pack(fill="both")
ttk.Button(buttons, text="Greet", command=greet).pack(side="left", fill="x", expand=True)
ttk.Button(buttons, text="Quit", command=root.destroy).pack(side="right", fill="x", expand=True)

root.mainloop()
