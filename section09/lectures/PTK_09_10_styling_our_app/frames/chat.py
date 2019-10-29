import tkinter as tk
from tkinter import ttk
import requests
from frames.message_window import MessageWindow

messages = [{"message": "Hello, world", "date": 15498487}]
message_labels = []


class Chat(ttk.Frame):
    def __init__(self, container, background, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.message_window = MessageWindow(self, background=background)
        self.message_window.grid(row=0, column=0, sticky="NSEW", pady=5)

        input_frame = ttk.Frame(self, style="Controls.TFrame", padding=10)
        input_frame.grid(row=1, column=0, sticky="EW")

        self.message_input = tk.Text(input_frame, height=3)
        self.message_input.pack(expand=True, fill="both", side="left", padx=(0, 10))

        message_submit = ttk.Button(
            input_frame,
            text="Send",
            style="SendButton.TButton",
            command=self.post_message
        )
        message_submit.pack()

        message_fetch = ttk.Button(
            input_frame,
            text="Fetch",
            style="FetchButton.TButton",
            command=self.get_messages
        )
        message_fetch.pack()
        self.message_window.update_message_widgets(messages, message_labels)
    
    def post_message(self):
        body = self.message_input.get("1.0", "end").strip()
        requests.post("http://167.99.63.70/message", json={"message": body})
        self.message_input.delete('1.0', "end")
        self.get_messages()

    def get_messages(self):
        global messages
        messages = requests.get("http://167.99.63.70/messages").json()
        self.message_window.update_message_widgets(messages, message_labels)
        self.after(150, lambda: self.message_window.yview_moveto(1.0))
