import tkinter as tk
from frames.chat import Chat


class Messenger(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("1200x500")
        self.minsize(800, 500)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.chat_frame = Chat(self)

        self.chat_frame.grid(row=0, column=0, sticky="NSEW")



root = Messenger()
root.mainloop()
