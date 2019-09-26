import tkinter as tk
from tkinter import ttk


def greet():
    print("Hello, World!")


root = tk.Tk()
# Window title is defined on root using the .title() method
root.title("Hello")

"""
Below we define a Frame using the .Frame() method.
Frames are general purpose rectangular grouping widgets for collecting widgets into a single group.
Frame takes an optional master positional argument, which defaults to None, and then a number of configuration options.

Frame(master=None, **options)

In our example, we specify root (the main application window) as the master of the Frame main.
As an optional config argument, we specify a padding value of 20px on all sides.
"""
# Padding is defined in pixels by default. Multiple values possible to specify padding in different directions.
main = ttk.Frame(root, padding=20)
main.pack(fill="both")

"""
Below we define two buttons, both of which are children of main.

The text keyword argument provided to the Button() method specifies the text content of the button.
The command keyword argument is the name of a function to call when the button is clicked.

When a user clicks the Greet button, we call the greet() function, printing "Hello, World!" to the terminal.
When a user clicks the Quit button, we call the root.destroy() method.

root.destroy() terminates the mainloop, and since all other widgets are children of root, they get destroyed along with it.
"""
greet_button = ttk.Button(main, text="Greet", command=greet)
greet_button.pack(side="left", fill="x", expand=True)

quit_button = ttk.Button(main, text="Quit", command=root.destroy)
quit_button.pack(side="right", fill="x", expand=True)

"""
Missing off the value for the expand parameter causes the buttons to stay the same size, centered in a pair of imaginary boxes
which is filling up the space as the page increases in size.
"""
# ttk.Button(main, text="Greet", command=greet).pack(side=LEFT, fill=X)
# ttk.Button(main, text="Quit", command=root.destroy).pack(side=RIGHT, fill=X)

"""
Missing off the value for the fill parameter means that the buttons will stay at the size defined by their text content, but
will remain stuck to the edges we defined using side.
"""
# ttk.Button(main, text="Greet", command=greet).pack(side=LEFT)
# ttk.Button(main, text="Quit", command=root.destroy).pack(side=RIGHT)

"""
By default, the buttons will stack underneath each other.
"""
# ttk.Button(main, text="Greet", command=greet).pack()
# ttk.Button(main, text="Quit", command=root.destroy).pack()

root.mainloop()
