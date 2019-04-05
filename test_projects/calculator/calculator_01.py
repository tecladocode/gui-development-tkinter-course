import tkinter as tk
from tkinter import ttk

"""
Right now the handle_click function simply takes a value specific to each button and prints it.
This is intended as a demonstration of how to pass in variables to Button commands.
In the standard case, they simply take a function name.
"""


def handle_click(x):
    print(x)


root = tk.Tk()
root.title("Calculator")

buttons = ttk.Frame(root, padding="10")
buttons.grid()

"""
Passing in a variable to a command can be easily achieved using a lambda function.

TODO: Another option exists using partials. This may be better, but I need to do more research.
TODO: I need to see if there is also a better way to deal with the amount of repetition in the following lines.
"""
ttk.Button(buttons, text="1").grid(column=0, row=0)
ttk.Button(buttons, text="2").grid(column=1, row=0)
ttk.Button(buttons, text="3").grid(column=2, row=0)
ttk.Button(buttons, text="/").grid(column=3, row=0)

ttk.Button(buttons, text="4").grid(column=0, row=1)
ttk.Button(buttons, text="5").grid(column=1, row=1)
ttk.Button(buttons, text="6").grid(column=2, row=1)
ttk.Button(buttons, text="*").grid(column=3, row=1)

ttk.Button(buttons, text="7").grid(column=0, row=2)
ttk.Button(buttons, text="8").grid(column=1, row=2)
ttk.Button(buttons, text="9").grid(column=2, row=2)
ttk.Button(buttons, text="-").grid(column=3, row=2)

ttk.Button(buttons, text=".").grid(column=0, row=3)
ttk.Button(buttons, text="0").grid(column=1, row=3)
ttk.Button(buttons, text="=").grid(column=2, row=3)
ttk.Button(buttons, text="+").grid(column=3, row=3)

"""
winfo is short for window information. The winfo_children() method gets all children of a container.
For each child, we get a reference like this:

.!frame.!button

which can be used to select a specific widget. As such, we can iterate over these widgets and call methods on them individually.
Below we call the grid_configure method, allowing us to specify x and y padding for each button in buttons.
"""
for child in buttons.winfo_children():
    child.grid_configure(padx=5, pady=5)
    child.configure(command=lambda button=child: handle_click(button["text"]))
    """
    child.configure(command=lambda: handle_click(child['text'])) did not solve the repetition issue.
    All of the values for child['text'] end up being "+", as child in the first line of the for loop shares an extended
    scope with child inside the lambda function.
    The value of child['text'] does not get evaluated until the function is called, by which time, the value of child is
    the button containing the text content, "+".

    Fixed the issue by setting a default value for a new lambda argument called button.
    Default arguments are evaluated when a function is created, not when they are called,
    meaning we can preserve the value of each iteration of child after the loop completes.
    """

root.mainloop()
