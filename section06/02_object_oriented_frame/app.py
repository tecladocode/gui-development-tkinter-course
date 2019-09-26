import tkinter as tk
from tkinter import ttk


class UserInputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.user_input = tk.StringVar()

        label = ttk.Label(self, text="Enter your name: ")
        entry = ttk.Entry(self)
        button = ttk.Button(self, command=self.greet)

        label.pack(side="left")
        entry.pack(side="left")
        button.pack(side="left")
    
    def greet(self):
        print(f"Hello, {self.user_input.get()}!")



root = tk.Tk()
frame = UserInputFrame(root)
frame.pack()

root.mainloop()