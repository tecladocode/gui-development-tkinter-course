import tkinter as tk
from tkinter import ttk
from frames import ScrollableFrame, BookingEdit


class BookingsOnDay(tk.Toplevel):
    def __init__(self, container, calendar, bookings):
        super().__init__(container)

        self.frame = ScrollableFrame(self, style="Background.TFrame")
        self.calendar = calendar

        ttk.Label(
            self.frame.scrollable_frame,
            text="Bookings",
            anchor="center",
            style="Title.TLabel",
        ).pack(fill="x", expand=True)

        for booking_id, name, date in bookings:  # TODO: Sort according to time of day
            booking_container = ttk.Frame(
                self.frame.scrollable_frame, style="Background.TFrame"
            )

            name_var = tk.StringVar(value=name)
            selected_date = tk.StringVar(value=date)

            # This is necessary so that the StringVar remains in memory and is not garbage collected
            booking_container.date = selected_date

            ttk.Label(booking_container, text=f"{name}", style="Field.TLabel").pack(
                side="left", padx=(20, 0)
            )
            ttk.Label(
                booking_container, textvariable=selected_date, style="Field.TLabel"
            ).pack(side="left", padx=(20, 0))
            ttk.Button(
                booking_container,
                text="Edit date",
                style="Secondary.TButton",
                command=lambda: self.create_edit_booking_frame(
                    booking_id, name_var, selected_date
                ),
            ).pack(side="left", padx=(50, 0))
            booking_container.pack(pady=10)

        self.frame.grid(row=0, column=0, sticky="NSEW")

    def create_edit_booking_frame(self, booking_id, name, date):
        booking_frame = BookingEdit(
            self, self.calendar, booking_id, name, date, self.frame.tkraise
        )
        booking_frame.grid(row=0, column=0, sticky="NSEW")
        booking_frame.tkraise()
