# TODO: Add labels to the plot axes, and add a graph title

from tkinter import ttk
import tkinter as tk

# Import animation to let us live update the plots.
import matplotlib.animation as animation

# Import matplotlib and define the backend to TkAgg to help it work with Tkinter.
from matplotlib.figure import Figure

# Gross import to grab the matplotlib canvas and the built in buttons to zoom and select, etc.
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib

matplotlib.use("TkAgg")


# Defines a matplotlib figure
fig = Figure(figsize=(5, 5), dpi=100)

# Convention seems to be to call these subplots a or ax
ax = fig.add_subplot(111)

"""
The animate function takes in an interval and allows us to continuously replot a matplotlib figure.

In this example, we grab some dummy data in csv format from dummyData.txt
We extract the data to two lists: x_vals and y_vals, then call plot to actually display the data.

ax.clear() here is a vital line, as it prevents us from painting over the same information every interval.
We need a fresh canvas each time we plot, or it'll become a total mess.
"""


def animate(i):
    with open("dummyData.txt", "r") as file:
        lines = [line.strip() for line in file.readlines()]

    x_vals = []
    y_vals = []

    for line in lines:
        x, y = line.split(",")
        x_vals.append(int(x))
        y_vals.append(int(y))

    ax.clear()
    ax.plot(x_vals, y_vals)

    """
    Tried this shorter alternative, but the fact that the values are strings keeps the y axis from being ordered.
    Leaving it here, because it highlights a potential error students might run into.

    lines = [line.split(",") for line in lines]
    x, y = zip(*(line for line in lines))
    
    ax.clear()
    ax.plot(x, y)
    """


class CurrencyConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Currency Converter")

        container = ttk.Frame(self)
        container.grid(padx=10, pady=10, sticky="EW")

        self.frames = {}

        # The comma below is important as we need an iterable object for for. Without it, it tries to iterate over the class.
        for F in (DummyData,):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="NSEW")

        self.show_frame(DummyData)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


class DummyData(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Define a canvas, passing in some figure object.
        canvas = FigureCanvasTkAgg(fig, self)

        # The show method paints our canvas. Until we actually call show, all the plotting is done in the backend.
        canvas.draw()
        canvas.get_tk_widget().pack()

        # This toolbar gives us the standard matplotlib buttons below our plot.
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack()


root = CurrencyConverter()

# Below we define the animation function behaviour. I needs to be assigned to something, but it doesn't appear to matter what.
# Convention seems to be using ani or anim as a variable name.
ani = animation.FuncAnimation(fig, animate, interval=1000)
root.mainloop()
