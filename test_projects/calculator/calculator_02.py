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

row_0 = ttk.Frame(buttons)
row_1 = ttk.Frame(buttons)
row_2 = ttk.Frame(buttons)
row_3 = ttk.Frame(buttons)

"""
Passing in a variable to a command can be easily achieved using a lambda function.

TODO: Another option exists using partials. This may be better, but I need to do more research.

Split the button grid into rows, allowing me to remove the row definition from each item,
adding them to the for loop later in the app.
"""
ttk.Button(row_0, text="1", command=lambda: handle_click("1")).grid(column=0)
ttk.Button(row_0, text="2", command=lambda: handle_click("2")).grid(column=1)
ttk.Button(row_0, text="3", command=lambda: handle_click("3")).grid(column=2)
ttk.Button(row_0, text="/", command=lambda: handle_click("/")).grid(column=3)

ttk.Button(row_1, text="4", command=lambda: handle_click("4")).grid(column=0)
ttk.Button(row_1, text="5", command=lambda: handle_click("5")).grid(column=1)
ttk.Button(row_1, text="6", command=lambda: handle_click("6")).grid(column=2)
ttk.Button(row_1, text="*", command=lambda: handle_click("*")).grid(column=3)

ttk.Button(row_2, text="7", command=lambda: handle_click("7")).grid(column=0)
ttk.Button(row_2, text="8", command=lambda: handle_click("8")).grid(column=1)
ttk.Button(row_2, text="9", command=lambda: handle_click("9")).grid(column=2)
ttk.Button(row_2, text="-", command=lambda: handle_click("-")).grid(column=3)

ttk.Button(row_3, text=".", command=lambda: handle_click(".")).grid(column=0)
ttk.Button(row_3, text="0", command=lambda: handle_click("0")).grid(column=1)
ttk.Button(row_3, text="=", command=lambda: handle_click("=")).grid(column=2)
ttk.Button(row_3, text="+", command=lambda: handle_click("+")).grid(column=3)

"""
winfo is short for window information. The winfo_children() method gets all children of a container.
For each child, we get a reference like this:

.!frame.!button

which can be used to select a specific widget. As such, we can iterate over these widgets and call methods on them individually.
Below we call the grid_configure method, allowing us to specify x and y padding for each button in buttons.
"""
for i, button_row in enumerate(buttons.winfo_children()):
    """
    Defined the grid for each item in the outer for loop, removing the need for individual definitions above.
    Not 100% sure if this is better, as it does make it harder to see what is happening in the program.
    I'm tempted to say that a DRY approach to Tkinter is maybe not ideal, as removing the repetition massively complicates things.
    """
    button_row.grid(row=i)

    for button in button_row.winfo_children():
        # row=0 is necessary to stop them trying to move onto independent rows.
        button.grid_configure(padx=5, pady=5, row=0)

root.mainloop()
