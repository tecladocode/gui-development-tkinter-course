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

The create_button function seeks to bypass the awkward solution to using a lamdba function with command, found in calculator_01.py
The argument to handle_click is now created when the button is created, allowing for an extensive reduction in the grid setup.

A pair of nested for loops and a list comprehension are used to generate the 16 buttons.
Each button is created by create_button, and positioned precisely using grid.

The innermost for loop now covered every element in the buttons group, meaning that we can do away with the for loop
featured in the previous calculator iterations.


        for button in button_row.winfo_children():
            button.grid_configure(padx=5, pady=5, row=1)


Note that the grid method cannot be called in the create_button function, but I have not found a concrete reason as to why yet.
Notice also that the buttons object above required that the grid method be called after the object was created.
This seems to be a common pattern.
"""


def create_button(text):
    return ttk.Button(buttons, text=text, command=lambda: handle_click(text))


texts = (
    ["1", "2", "3", "/"],
    ["4", "5", "6", "*"],
    ["7", "8", "9", "-"],
    [".", "0", "=", "+"],
)

for i, text_group in enumerate(texts):
    button_row = [create_button(text) for text in text_group]

    for j, button in enumerate(button_row):
        button.grid(column=j, row=i, padx=5, pady=5)

root.mainloop()
