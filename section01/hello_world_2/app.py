from tkinter import *
from tkinter import ttk

def greet():
    print("Hello, World!")

root = Tk()
root.title("Hello")    # Window title is defined on root using the .title() method

"""
Below we define a Frame using the .Frame() method.
Frames are general purpose rectangular grouping widgets for collecting widgets into a single group.
Frame takes an optional master positional argument, which defaults to None, and then a number of configuration options.

Frame(master=None, **options)

In our example, we specify root (the main application window) as the master of the Frame main.
As an optional config argument, we specify a padding value of 20px on all sides.
"""
main = ttk.Frame(root, padding="20")    # Padding is defined in pixels by default. Multiple values possible to specify padding in different directions.
main.grid() # Grid is used to create a table like structure. Various positional arguments can be provided, but we have provided none.

"""
Below we define two buttons, both of which are children of main.
Once again we use the .grid() method, this time specifying column and row position of the elements within the container grid.

The text keyword argument provided to the Button() method specifies the text content of the button.
The command keyword argument is the name of a function to call when the button is clicked.

When a user clicks the Greet button, we call the greet() function, printing "Hello, World!" to the terminal.
When a user clicks the Quit button, we call the root.destroy() method.

root.destroy() terminates the mainloop, and since all other widgets are children of root, they get destroyed along with it.
"""
ttk.Button(main, text = "Greet", command = greet).grid(column = 1, row = 1)
ttk.Button(main, text = "Quit", command = root.destroy).grid(column = 2, row = 1)

root.mainloop()
