# TODO: Add labels to the plot axes, and add a graph title

import json
import requests
from tkinter import ttk
import tkinter as tk
import matplotlib.animation as animation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib

matplotlib.use("TkAgg")


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

url = "https://free.currencyconverterapi.com/api/v6/convert?q=USD_GBP&compact=ultra&date=2019-01-01&endDate=2019-01-09&apiKey=443eaf8aa1f431564727"

fig = Figure(figsize=(10, 5), dpi=100)
a = fig.add_subplot(111)


def animate(i):
    data = requests.get(url)
    json_data = data.json()

    dates, rates = zip(*json_data["USD_GBP"].items())

    a.clear()
    a.plot(dates, rates)


class CurrencyConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Currency Converter")

        container = ttk.Frame(self)
        container.grid(padx=10, pady=10, sticky="EW")

        self.frames = {}

        for F in (Home, HistoricalData):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="NESW")

        self.show_frame(Home)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


class Home(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        button = ttk.Button(
            self,
            text="Historical Data",
            command=lambda: controller.show_frame(HistoricalData),
        )
        button.pack()


class HistoricalData(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().pack()

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack()


root = CurrencyConverter()
# Request every 60 seconds, since we are strictly limited by the API
ani = animation.FuncAnimation(fig, animate, interval=60000)
root.mainloop()
