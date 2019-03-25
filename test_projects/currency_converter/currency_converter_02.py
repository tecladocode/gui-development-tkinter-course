# https://free.currencyconverterapi.com/

# Import matplotlib and define the backend to TkAgg to help it work with Tkinter.
import matplotlib
matplotlib.use("TkAgg")

# Gross import to grab the matplotlib canvas and the built in buttons to zoom and select, etc.
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

# Import animation to let us live update the plots.
import matplotlib.animation as animation

from tkinter import *
from tkinter import ttk

import requests
import json

"""
Grab historical USD value data from free.currencyconverterapi.com
Data is limited to a span of 8 days. Values are an average for the day.

The format of the data is as follows:

    {
        "<currency_1>_<currency_2>": {
            "<date_1>": <exchange rate>,
            "<date_2>": <exchange rate>
            ...
        },
        "<currency _2>_<currency_1>": {
            "<date_1>": <exchange rate>,
            "<date_2>": <exchange rate>
            ...
        }
    }

The API is relatively simple. Docs can be found here: https://www.currencyconverterapi.com/docs
"""

url = "https://free.currencyconverterapi.com/api/v6/convert?q=USD_GBP,GBP_USD&compact=ultra&date=2019-01-01&endDate=2019-01-09&apiKey=443eaf8aa1f431564727"
data = requests.get(url)
json_data = data.json()

fig = Figure(figsize=(5,5), dpi=100)
animated_subplot = fig.add_subplot(111)

def animate(i):
    pass

class CurrencyConverter(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title("Currency Converter")

        container = ttk.Frame(self)
        container.grid(padx = 10, pady = 10, sticky = (E, W))
        
        self.frames = {}

        for F in (Home, HistoricalData):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = (N, S, E, W))

        self.show_frame(Home)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


class Home(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)


class HistoricalData(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)


root = CurrencyConverter()
# ani = animation.FuncAnimation(fig, animate, interval=1000)
root.mainloop()
