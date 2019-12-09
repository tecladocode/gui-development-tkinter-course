import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from frames import Home
from windows import BookingCalendar
from windows.bookings_on_day import NewBooking
from database import close_database_connection
import colors as Colors

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


class Bookings(tk.Tk):
    def __init__(self):
        super().__init__()

        self["background"] = Colors.BACKGROUND

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        home = Home(
            self,
            lambda: self.show_frame(NewBooking),
            lambda: self.show_frame(BookingCalendar),
        )
        new_booking = NewBooking(self, lambda: self.show_frame(Home))
        booking_calendar = BookingCalendar(self, lambda: self.show_frame(Home))

        home.grid(row=0, column=0, sticky="NSEW")
        new_booking.grid(row=0, column=0, sticky="NSEW")
        booking_calendar.grid(row=0, column=0, sticky="NSEW")

        self.frames = {
            Home: home,
            NewBooking: new_booking,
            BookingCalendar: booking_calendar,
        }
        self.show_frame(Home)

    def show_frame(self, frame):
        self.frames[frame].tkraise()


root = Bookings()

style = ttk.Style(root)
style.theme_use("clam")

default_font = font.nametofont("TkDefaultFont").copy()
default_font.config(size=18)

primary_button_font = font.nametofont("TkDefaultFont").copy()
primary_button_font.config(weight="bold")

style.configure("Background.TFrame", background=Colors.BACKGROUND)

style.configure(
    "Title.TLabel", font=default_font, padding=10, background=Colors.BACKGROUND
)

style.configure("Field.TLabel", background=Colors.BACKGROUND)

style.configure(
    "Primary.TButton",
    background=Colors.PRIMARY,
    foreground="white",
    font=primary_button_font,
    padding=10,
)
style.map(
    "Primary.TButton",
    background=[("pressed", Colors.BUTTON_PRESSED), ("active", Colors.BUTTON_ACTIVE)],
)
style.configure("Secondary.TButton", background=Colors.SECONDARY, padding=10)

style.configure("LargeEntry.TEntry", padding=5)
style.configure("LargeEntry.TCombobox", padding=5)
style.map("LargeEntry.TEntry", background=[("disabled", Colors.DISABLED)])

root.mainloop()
close_database_connection()
