import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from frames.chat import Chat

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

COLOUR_LIGHT_BACKGROUND_1 = "#fff"
COLOUR_LIGHT_BACKGROUND_2 = "#f2f3f5"
COLOUR_LIGHT_BACKGROUND_3 = "#e3e5e8"

COLOUR_DARK_BACKGROUND_1 = "#36393f"
COLOUR_DARK_BACKGROUND_2 = "#2f3136"
COLOUR_DARK_BACKGROUND_3 = "#202225"

COLOUR_LIGHT_TEXT = "#aaa"

COLOUR_BUTTON_NORMAL = "#5fba7d"
COLOUR_BUTTON_ACTIVE = "#58c77c"
COLOUR_BUTTON_PRESSED = "#44e378"


class Messenger(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("1400x500")
        self.minsize(1400, 500)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.chat_frame = Chat(
            self,
            background=COLOUR_LIGHT_BACKGROUND_3,
            style="Messages.TFrame"
        )

        self.chat_frame.grid(row=0, column=0, sticky="NSEW")



root = Messenger()
root.tk.call('tk', 'scaling', 3.0)

font.nametofont("TkDefaultFont").configure(size=14)

style = ttk.Style(root)
style.theme_use("clam")

style.configure("Messages.TFrame", background=COLOUR_LIGHT_BACKGROUND_3)
# style.configure("DarkMessages.TFrame", background=COLOUR_DARK_BACKGROUND_3)

style.configure("Controls.TFrame", background=COLOUR_LIGHT_BACKGROUND_2)
# style.configure("DarkControls.TFrame", background=COLOUR_DARK_BACKGROUND_2)

style.configure("SendButton.TButton", borderwidth=0, background=COLOUR_BUTTON_NORMAL)
style.map(
    "SendButton.TButton",
    background=[("pressed", COLOUR_BUTTON_PRESSED), ("active", COLOUR_BUTTON_ACTIVE)],
)

style.configure(
    "FetchButton.TButton", background=COLOUR_LIGHT_BACKGROUND_1, borderwidth=0
)

# style.configure(
#     "DarkFetchButton.TButton", background=COLOUR_DARK_BACKGROUND_1, borderwidth=0
# )

style.configure("Message.TMessage", background=COLOUR_LIGHT_BACKGROUND_2, padding=5)
# style.configure("DarkMessage.TMessage", background=COLOUR_DARK_BACKGROUND_2, padding=5)

style.configure(
    "Time.TLabel",
    padding=5,
    background=COLOUR_LIGHT_BACKGROUND_1,
    foreground=COLOUR_LIGHT_TEXT,
    font=("TkDefaultFont", 8)
)
# style.configure(
#     "DarkTime.TLabel",
#     padding=5,
#     background=COLOUR_DARK_BACKGROUND_1,
#     foreground=COLOUR_LIGHT_TEXT,
#     font=8
# )

root.mainloop()
