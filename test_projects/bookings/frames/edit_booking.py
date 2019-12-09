import tkinter as tk
from tkinter import ttk
import datetime
from tkcalendar import DateEntry


class BookingEdit(ttk.Frame):
    def __init__(self, container, calendar, booking_id, name, date, hide_frame):
        super().__init__(container, style="Background.TFrame")

        self.calendar = calendar
        self.selected_date = date
        selected_datetime_instance = datetime.datetime.strptime(
            self.selected_date.get(), "%d-%m-%Y"
        )
        self.columnconfigure((0, 1), weight=1)

        ttk.Label(self, text="Edit booking", style="Title.TLabel").grid(
            row=0, column=0, columnspan=2
        )

        ttk.Label(self, text="Name: ", style="Field.TLabel").grid(row=1, column=0)
        self.name = ttk.Entry(
            self, textvariable=name, state="disabled", style="LargeEntry.TEntry"
        )
        self.name.grid(row=1, column=1, sticky="EW")

        ttk.Label(self, text="Booking Date: ", style="Field.TLabel").grid(
            row=2, column=0
        )

        self.date = DateEntry(
            self,
            textvariable=self.selected_date,
            date_pattern="dd-mm-yyyy",
            year=selected_datetime_instance.year,
            month=selected_datetime_instance.month,
            day=selected_datetime_instance.day,
            style="LargeEntry.TCombobox",
        )
        self.date.grid(row=2, column=1, sticky="EW")

        for widget in self.winfo_children():
            widget.grid_configure(padx=10, pady=10)

        button_frame = ttk.Frame(self, style="Background.TFrame")
        button_frame.grid(row=3, column=0, columnspan=2)

        ttk.Button(
            button_frame,
            text="Update date",
            style="Primary.TButton",
            command=lambda: self.update_booking_date(booking_id),
        ).pack(side="right", padx=10, pady=10)

        ttk.Button(
            button_frame, text="Close", style="Secondary.TButton", command=hide_frame
        ).pack(side="right", padx=10, pady=10)

    def update_booking_date(self, booking_id):
        selected_date = datetime.datetime.strptime(self.selected_date.get(), "%d-%m-%Y")
        self.calendar.calevent_configure(booking_id, date=selected_date)
