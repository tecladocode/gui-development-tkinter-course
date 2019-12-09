from tkinter import ttk
from tkcalendar import DateEntry
from database import add_booking


class NewBooking(ttk.Frame):
    def __init__(self, container, open_home):
        super().__init__(container, style="Background.TFrame")

        self.columnconfigure(1, weight=1)

        ttk.Label(self, text="New Booking", style="Title.TLabel").grid(
            row=0, column=0, columnspan=2
        )

        ttk.Label(self, text="Name: ", style="Field.TLabel").grid(row=1, column=0)
        self.name = ttk.Entry(self, style="LargeEntry.TEntry")
        self.name.grid(row=1, column=1, sticky="EW")

        # TODO: Prevent two people booking the same time
        ttk.Label(self, text="Time: ", style="Field.TLabel").grid(row=2, column=0)
        self.time = ttk.Entry(self, style="LargeEntry.TEntry")
        self.time.insert("end", "09:00")
        self.time.grid(row=2, column=1, sticky="EW")

        ttk.Label(self, text="Booking Date: ", style="Field.TLabel").grid(
            row=3, column=0
        )
        self.date = DateEntry(
            self, date_pattern="dd-mm-yyyy", style="LargeEntry.TCombobox"
        )
        self.date.grid(row=3, column=1, sticky="EW")

        button_frame = ttk.Frame(self, style="Background.TFrame")
        button_frame.grid(row=4, column=0, columnspan=2)

        ttk.Button(
            button_frame,
            text="Create booking",
            style="Primary.TButton",
            command=self.create_booking,
        ).pack(side="right", padx=10)

        ttk.Button(
            button_frame, text="Back", style="Secondary.TButton", command=open_home
        ).pack(side="right")

        for widget in self.winfo_children():
            widget.grid_configure(padx=10, pady=10)

    def create_booking(self):
        booking_date = self.date.get_date()
        hour, minute = map(int, self.time.get().split(":"))
        add_booking(
            self.name.get(),
            minute,
            hour,
            booking_date.day,
            booking_date.month,
            booking_date.year,
        )

        self.name.delete(0, "end")
        self.time.delete(0, "end")
