import tkinter as tk
from tkinter import ttk

"""
While calculate_feet doesn't use any arguments for its main logic, we later specify
that when a user uses the return key, this function will run. If we do not allow
for positional arguments, pressing return will give use an error:

    TypeError: calculate_feet() takes 0 positional arguments but 1 was given

In our case, the argument passed in is a KeyPress event object:

    <KeyPress event state=Mod2|0x2000 keysym=Return keycode=36 char='\r' x=76 y=38>
"""


def calculate_feet(*args):
    try:
        """
        The get() method is used to fetch the value of a StringVar() instance.

        The set() method is the counterpart of get() and sets the value of 
        a StringVar() instance.
        """
        value = float(metres_value.get())
        feet_value.set(value * 3.28084)
    except ValueError:
        # For now we're just going to ignore faulty inputs to the converter
        pass


root = tk.Tk()
root.title("Distance Converter")

main = ttk.Frame(root, padding="30 15 30 15")
main.grid()

"""
We configure root to have a single row and column, with weight (importance / priority) set to 1.
This means that as the window expands, priority is given to this row to expand,
allowing it to stretch to the window size in both directions.
"""
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


# Here we create two instances of the StringVar() class, which is to track the content of widgets
feet_value = tk.StringVar()
metres_value = tk.StringVar()

"""
Below we use a few new properties, and a new widget type.

The Entry widget is used to accept text input of some type, and works very much like
    
    <input type="text">

in HTML. It's a single line box that accepts a string of characters.

We also dfine a specific width for this input box. Width does not take a pixel value,
but rather a character size. It therefore functions like ems. It's possible to define the 
character to use for these character based size measurements. Obviously for monospace fonts,
the character chosen doesn't matter, but for variable width fonts, it can make a major difference:

    font.measure("m")

A final point of note is the textvariable keyword argument used with Entry. This associates a variable
with the content of the Entry field. As such, the value of metres_value will update automatically
as the content of metres_input gets updated.
"""
metres_input = ttk.Entry(main, width=10, textvariable=metres_value)

"""
The sticky property below anchors a widget to the edges of its container. Compass directions
are used to specify this behaviour. You can pass in a tuple of values to anchor a widget to more than
one edge.
"""
metres_input.grid(column=2, row=1, sticky="EW")


"""
Once again we specify a textvariable argument, but for Label it behaves differently to input.
For a label, the text content of that lable updates when the value of the associated variable
changes. As such, when the value of feet_value changes, the text content of this Label will be
instantly updated. 
"""
ttk.Label(main, textvariable=feet_value).grid(column=2, row=2, sticky="EW")
ttk.Button(main, text="Calculate", command=calculate_feet).grid(
    column=1, row=3, columnspan=2, sticky="EW"
)

ttk.Label(main, text="metres").grid(column=1, row=1, sticky="W", ipadx=5)
ttk.Label(main, text="feet").grid(column=1, row=2, sticky="W", ipadx=5)

for child in main.winfo_children():
    child.grid_configure(padx=5, pady=5)

# We can specify a default focus using the focus method on a widget.
metres_input.focus()

"""
Below we use the bind method to call the calculate_feet function in response to some even.
In this instance, the event is pressing the return key on the keyboard.

Note that bind is attached to a specific element, so it's possible to trigger behaviour only for
certain frames. By binding to root, this event will be triggered for all frames, since they are
all children of root.
"""
root.bind("<Return>", calculate_feet)
# This bind is for the enter key on a numpad
root.bind("<KP_Enter>", calculate_feet)

root.mainloop()
