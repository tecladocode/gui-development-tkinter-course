import tkinter as tk
from tkinter import ttk
import requests

messages = [{"message": "Hello, world", "date": 15498487}]
message_labels = []


class Chat(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.messages_frame = ttk.Frame(self)
        self.messages_frame.grid(row=0, column=0, sticky="NSEW", pady=5)

        input_frame = ttk.Frame(self, padding=10)
        input_frame.grid(row=1, column=0, sticky="EW")

        message_fetch = ttk.Button(
            input_frame,
            text="Fetch",
            command=self.get_messages
        )
        message_fetch.pack()

    def get_messages(self):
        global messages
        messages = requests.get("http://167.99.63.70/messages").json()
        self.update_message_widgets()
    
    def update_message_widgets(self):
        existing_labels = [
            message["text"] for message in message_labels
        ]

        for message in messages:
            if message["message"] not in existing_labels:
                new_message = ttk.Label(
                    self.messages_frame,
                    text=message["message"],
                    anchor="w",
                    justify="left"
                )

                new_message.grid(sticky="NSEW")

                message_labels.append(new_message)
