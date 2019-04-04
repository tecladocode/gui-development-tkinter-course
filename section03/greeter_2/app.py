import tkinter as tk
from tkinter import ttk


def greet(*args):
    name = user_name.get()
    greeting_message.set(f"Hello, {name or 'World'}!")
    greeting.grid(row=2, column=1, columnspan=2, sticky="W", pady=(10, 0))


root = tk.Tk()
root.title("Greeter")

user_name = tk.StringVar()
greeting_message = tk.StringVar()

frame = ttk.Frame(root, padding=(20, 10, 20, 0))
frame.grid()

root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

name_label = ttk.Label(frame, text="Name:")
name_label.grid(row=1, column=1, padx=(0, 10))

name_entry = ttk.Entry(frame, width=15, textvariable=user_name)
name_entry.grid(row=1, column=2)

greeting = ttk.Label(frame, textvariable=greeting_message)

buttons = ttk.Frame(frame, padding=(0, 10))
buttons.grid(row=3, column=1, columnspan=2, sticky="EW")

greet_button = ttk.Button(buttons, text="Greet", command=greet)
greet_button.grid(row=1, column=1, sticky="W")

quit_button = ttk.Button(buttons, text="Quit", command=root.destroy)
quit_button.grid(row=1, column=2, sticky="E")

root.bind("<Return>", greet)
root.bind("KP_Enter", greet)

root.mainloop()

