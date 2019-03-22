# https://free.currencyconverterapi.com/

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



"""
Added some boilerplate below. Currency this will raise an exception.
"""
class CurrencyConverter(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title("Currency Converter")

        container = ttk.Frame(self)
        container.grid(padx = 10, pady = 10, sticky = (E, W))
        
        self.frames = {}

        for F in ():
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = (N, S, E, W))

        self.show_frame()

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

root = CurrencyConverter()
root.mainloop()
