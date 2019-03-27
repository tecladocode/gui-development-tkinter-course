from tkinter import *
from tkinter import ttk

def greet():
    # The get() method is used to fetch the value of a StringVar() instance.
    print(f"Hello, {user_name.get() or 'World'}!")  # If user_name is empty, print Hello, World!

root = Tk()
root.title("Greeter")

# Here we create an instances of the StringVar() class, which is to track the content of widgets
user_name = StringVar()

# We define two frames to keep the input on different lines. In the next version we will switch to grid() geometry.
input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))  # Padding accepts a tuple of up to four values. Clockwise like CSS.
input_frame.pack(fill=BOTH)
ttk.Label(input_frame, text="Name: ").pack(side=LEFT)
name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name).pack(side=LEFT)

buttons = ttk.Frame(root, padding=(20, 10))
buttons.pack(fill=BOTH)
ttk.Button(buttons, text="Greet", command=greet).pack(side=LEFT, fill=X, expand=True)
ttk.Button(buttons, text="Quit", command=root.destroy).pack(side=RIGHT, fill=X, expand=True)

root.mainloop()
