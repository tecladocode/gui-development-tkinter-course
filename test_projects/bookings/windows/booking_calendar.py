from tkinter import ttk
import datetime
from tkcalendar import Calendar
from database import get_bookings
from windows.bookings_on_day import BookingsOnDay
import colors as Colors


class BookingCalendar(ttk.Frame):
    def __init__(self, container, open_home):
        super().__init__(container, style="Background.TFrame")

        today = datetime.datetime.now()
        self.bookings = []

        ttk.Label(self, text="Calendar", style="Title.TLabel").pack()
        self.calendar = Calendar(
            self,
            locale="en_GB",
            cursor="hand2",
            date_pattern="dd-mm-yyyy",
            showothermonthdays=False,
        )
        self.calendar.bind("<<CalendarMonthChanged>>", self._refresh_bookings)

        # This with .after because we need to wait until the theme has been changed to override styles.
        self.after(
            50, lambda: self.calendar.tag_config("booking", background=Colors.PRIMARY)
        )
        self._refresh_bookings()

        self.calendar.pack(fill="both", expand=True)
        self.calendar.bind("<<CalendarSelected>>", self.print_booking_info)

        button_frame = ttk.Frame(self, style="Background.TFrame")
        button_frame.pack(padx=10, pady=10)

        ttk.Button(
            button_frame, text="Back", style="Secondary.TButton", command=open_home
        ).pack(side="left", padx=(0, 10))

        ttk.Button(
            button_frame,
            text="Refresh",
            style="Secondary.TButton",
            command=self._refresh_bookings,
        ).pack(side="left")

    def _refresh_bookings(self, e=None):
        month, year = self.calendar.get_displayed_month()
        self.bookings = get_bookings(month, year)
        self.calendar.calevent_remove("all")

        for booking in self.bookings:
            booking_date = datetime.datetime(
                minute=booking[1],
                hour=booking[2],
                day=booking[3],
                month=booking[4],
                year=booking[5],
            )
            self.calendar.calevent_create(booking_date, booking[0], "booking")

    def print_booking_info(self, event):
        booking_ids = self.calendar.get_calevents(event.widget.selection_get())
        booking_names = [
            self.calendar.calevent_cget(_id, "text") for _id in booking_ids
        ]
        booking_times = [
            self.calendar.calevent_cget(_id, "date") for _id in booking_ids
        ]

        booking_data = [
            (_id, name, time)
            for _id, name, time in zip(booking_ids, booking_names, booking_times)
        ]

        if not booking_data:
            print("No bookings on", self.calendar.get_date())
        else:
            BookingsOnDay(self, self.calendar, booking_data)
