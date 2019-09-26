import tkinter as tk
from tkinter import ttk


def greet(*args):
    name = user_name.get()
    greeting_message.set(f"Hello, {name or 'World'}!")
    greeting.grid(row=1, column=0, columnspan=2, sticky="W", pady=(10, 0))


root = tk.Tk()
root.title("Greeter")

user_name = tk.StringVar()
greeting_message = tk.StringVar()

main = ttk.Frame(root, padding=(20, 10, 20, 0))
main.grid()

root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

name_label = ttk.Label(main, text="Name:")
name_label.grid(row=0, column=0, padx=(0, 10))
name_entry = ttk.Entry(main, width=15, textvariable=user_name)
name_entry.grid(row=0, column=1)
name_entry.focus()

greeting = ttk.Label(main, textvariable=greeting_message)

buttons = ttk.Frame(main, padding=(0, 10))
buttons.grid(row=2, column=0, columnspan=2, sticky="EW")

# buttons.columnconfigure(0, weight=1)
# buttons.columnconfigure(1, weight=1)
buttons.columnconfigure((0, 1), weight=1)

greet_button = ttk.Button(buttons, text="Greet", command=greet)
greet_button.grid(row=0, column=0, sticky="EW")
quit_button = ttk.Button(buttons, text="Quit", command=root.destroy)
quit_button.grid(row=0, column=1, sticky="EW")

root.bind("<Return>", greet)
root.bind("KP_Enter", greet)

root.mainloop()

