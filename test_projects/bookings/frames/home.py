from tkinter import ttk
from windows import BookingCalendar


class Home(ttk.Frame):
    def __init__(self, container, open_new_booking, open_booking_calendar):
        super().__init__(container, style="Background.TFrame")

        ttk.Label(self, text="Bookings", style="Title.TLabel").pack()
        ttk.Button(
            self, text="New Booking", style="Primary.TButton", command=open_new_booking
        ).pack(padx=10, pady=10)
        ttk.Button(
            self,
            text="Booking Calendar",
            style="Primary.TButton",
            command=open_booking_calendar,
        ).pack(padx=10, pady=10)
