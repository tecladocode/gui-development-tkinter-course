# In Python 3, the correct import is tkinter not Tkinter. Tkinter was the name of the module used for Python 2
import tkinter as tk

# ttk is the Python binding to the newer "themed widgets" added in Tk version 8.5
from tkinter import ttk

root = tk.Tk()
ttk.Label(root, text="Hello, World!", padding=(30, 10)).pack()

root.mainloop()
