from tkinter import *
from tkinter import ttk

"""
Right now the handle_click function simply takes a value specific to each button and prints it.
This is intended as a demonstration of how to pass in variables to Button commands.
In the standard case, they simply take a function name.
"""
def handle_click(x):
    print(x)

root = Tk()
root.title("Calculator")

buttons = ttk.Frame(root, padding = "10")
buttons.grid()

"""
Passing in a variable to a command can be easily achieved using a lambda function.

TODO: Another option exists using partials. This may be better, but I need to do more research.
TODO: I need to see if there is also a better way to deal with the amount of repetition in the following lines.
"""
ttk.Button(buttons, text = "1", command = lambda: handle_click("1")).grid(column = 1, row = 1)
ttk.Button(buttons, text = "2", command = lambda: handle_click("2")).grid(column = 2, row = 1)
ttk.Button(buttons, text = "3", command = lambda: handle_click("3")).grid(column = 3, row = 1)
ttk.Button(buttons, text = "/", command = lambda: handle_click("/")).grid(column = 4, row = 1)

ttk.Button(buttons, text = "4", command = lambda: handle_click("4")).grid(column = 1, row = 2)
ttk.Button(buttons, text = "5", command = lambda: handle_click("5")).grid(column = 2, row = 2)
ttk.Button(buttons, text = "6", command = lambda: handle_click("6")).grid(column = 3, row = 2)
ttk.Button(buttons, text = "*", command = lambda: handle_click("*")).grid(column = 4, row = 2)

ttk.Button(buttons, text = "7", command = lambda: handle_click("7")).grid(column = 1, row = 3)
ttk.Button(buttons, text = "8", command = lambda: handle_click("8")).grid(column = 2, row = 3)
ttk.Button(buttons, text = "9", command = lambda: handle_click("9")).grid(column = 3, row = 3)
ttk.Button(buttons, text = "-", command = lambda: handle_click("-")).grid(column = 4, row = 3)

ttk.Button(buttons, text = ".", command = lambda: handle_click(".")).grid(column = 1, row = 4)
ttk.Button(buttons, text = "0", command = lambda: handle_click("0")).grid(column = 2, row = 4)
ttk.Button(buttons, text = "=", command = lambda: handle_click("=")).grid(column = 3, row = 4)
ttk.Button(buttons, text = "+", command = lambda: handle_click("+")).grid(column = 4, row = 4)

"""
winfo is short for window information. The winfo_children() method gets all children of a container.
For each child, we get a reference like this:

.!frame.!button

which can be used to select a specific widget. As such, we can iterate over these widgets and call methods on them individually.
Below we call the grid_configure method, allowing us to specify x and y padding for each button in buttons.
"""
for child in buttons.winfo_children():
    child.grid_configure(padx = 5, pady = 5)

root.mainloop()
