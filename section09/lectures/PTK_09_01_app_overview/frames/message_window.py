import datetime
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


MAX_MESSAGE_WIDTH = 800

SCREEN_SIZE_TO_MESSAGE_WIDTH = {
    3000: 2000,
    2200: 1600,
    1800: 1100
}

class MessageWindow(tk.Canvas):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs, highlightthickness=0)

        self.messages_frame = ttk.Frame(container, style="Messages.TFrame")
        self.messages_frame.columnconfigure(0, weight=1)

        self.scrollable_window = self.create_window((0, 0), window=self.messages_frame, anchor="nw", width=self.winfo_width())

        def configure_scroll_region(event):
            self.configure(scrollregion=(0, 0, self.messages_frame.winfo_width(), self.bbox("all")[3]))
        
        def configure_canvas_size(event):
            self.configure(width=self.winfo_width())
            self.itemconfig(self.scrollable_window, width=self.winfo_width())

        self.bind("<Configure>", configure_canvas_size)
        self.messages_frame.bind("<Configure>", configure_scroll_region)
        self.bind_all("<MouseWheel>", self._on_mousewheel)

        scrollbar = ttk.Scrollbar(container, orient="vertical", command=self.yview)
        scrollbar.grid(row=0, column=1, sticky="NS")

        self.configure(yscrollcommand=scrollbar.set)
        self.yview_moveto(1.0)
    
    # https://stackoverflow.com/a/17457843/1587271
    def _on_mousewheel(self, event):
        self.yview_scroll(-int(event.delta/120), "units")

    def update_message_widgets(self, messages, message_labels):
        existing_labels = [
            (message["text"], time["text"]) for message, time in message_labels
        ]

        for message in messages:
            message_time = datetime.datetime.fromtimestamp(message["date"]).strftime(
                "%d-%m-%Y %H:%M:%S"
            )

            if (message["message"], message_time) not in existing_labels:
                self._create_message_container(message["message"], message_time, message_labels)
    
    def _create_message_container(self, message_content, message_time, message_labels):
        container = ttk.Frame(self.messages_frame, style="Messages.TFrame")
        container.columnconfigure(1, weight=1)
        container.grid(sticky="EW", padx=(10, 50), pady=10)

        def reconfigure_message_labels(event):
            for label, _ in message_labels:
                if label.winfo_width() < container.winfo_width():
                    label.configure(wraplength=min(container.winfo_width() - 130, MAX_MESSAGE_WIDTH))  # image width, frame padx, and image padx
            self.messages_frame.update()
        
        def reconfigure_message_labels(event):
            closest_break_point = min(SCREEN_SIZE_TO_MESSAGE_WIDTH.keys(), key=lambda b: abs(b - container.winfo_width()))
            for label, _ in message_labels:
                if label.winfo_width() < closest_break_point:
                    label.configure(wraplength=SCREEN_SIZE_TO_MESSAGE_WIDTH[closest_break_point])
            self.messages_frame.update()

        container.bind("<Configure>", reconfigure_message_labels)
        self._create_message_bubble(container, message_content, message_time, message_labels)
    
    def _create_message_bubble(self, container, message_content, message_time, message_labels):
        avatar_image = Image.open("./assets/male.png")
        avatar_photo = ImageTk.PhotoImage(avatar_image)

        avatar_label = tk.Label(
            container,
            image=avatar_photo,
            background="#e3e5e8"
        )

        avatar_label.image = avatar_photo
        avatar_label.grid(
            row=0,
            column=0,
            rowspan=2,
            sticky="NEW",
            padx=(0, 10),
            pady=(5, 0)
        )

        time_label = ttk.Label(
            container,
            text=message_time,
            style="Time.TLabel"
        )

        time_label.grid(row=0, column=1, sticky="NEW")

        message_label = tk.Label(
            container,
            text=message_content,
            wraplength=1100,
            justify="left",
            anchor="w", 
            background="#f2f3f5"
        )

        message_label.grid(row=1, column=1, sticky="NEW")

        message_labels.append((message_label, time_label))
