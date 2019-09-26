import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

set_dpi_awareness()


def greet(*args):
    print(f"Hello, {user_name.get()}!")


# Do not create the Style() database before initialising a window, as it will create one
# style = ttk.Style()

root = tk.Tk()
root.resizable(False, False)
root.title("Greeter")

# Create it after instead
style = ttk.Style(root)  # Pass in which application this style is for.

# Get the themes available in your system
print(style.theme_names())

print(style.theme_use())
print(style.theme_use("default"))

main = ttk.Frame(root, padding=(40, 20))
main.grid()

user_name = tk.StringVar()

name_label = ttk.Label(main, text="Name:")
name_label.grid(row=0, column=0, padx=(0, 10))
name_entry = ttk.Entry(main, width=15, textvariable=user_name)
name_entry.grid(row=0, column=1, padx=10)
name_entry.focus()

greet_button = ttk.Button(main, text="Greet", command=greet, style="PomodoroButton.TButton")
greet_button.grid(row=0, column=2, sticky="EW", padx=10)

root.mainloop()

