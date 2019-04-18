import tkinter as tk
from tkinter import ttk
import os  # Imported to allow for finding the calculator icon


class CalculatorApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        # Initialise Tkinter along with the MainApplication
        super().__init__(*args, **kwargs)

        # Create an encompassing Frame called container.
        container = ttk.Frame(self)
        container.grid(padx=10, pady=10)

        # Assign an instance of the Buttons class to the variable buttons
        buttons = Buttons(container, self)

        """
        We can define a dictionary called frames which will allow us to store references to
        our various views in the application. This means we can change the view in response
        to some event. See the show_frame method below. 
        """
        self.frames = {}
        # Create an entry in the dictionary for the Buttons frame
        self.frames[Buttons] = buttons

        buttons.grid()

        # We use the show_frame method to set the current view to the Buttons Frame
        self.show_frame(Buttons)

    def show_frame(self, container):
        """
        The show_frame method calls the tkraise method on a specific frame, bringing it to 
        the topmost layer of a window. Frames are then stacked on top of one another, with the
        topmost Frame obscuring the view to the ones below.

        The show_frame method takes a container as an argument and searches the frames dictionary
        defined above for a key matching the name of that container. The value of that container
        is then assigned to the frame variable, and raised to the topmost level of the stack.
        """

        frame = self.frames[container]
        frame.tkraise()


class Buttons(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        texts = (
            ["1", "2", "3", "/"],
            ["4", "5", "6", "*"],
            ["7", "8", "9", "-"],
            [".", "0", "=", "+"],
        )

        for i, text_group in enumerate(texts):
            button_row = [self.create_button(text) for text in text_group]

            for j, button in enumerate(button_row):
                button.grid(column=j, row=i, padx=5, pady=5)

    def create_button(self, text):
        return ttk.Button(text=text, command=lambda: self.handle_click(text))

    def handle_click(self, x):
        print(x)


root = CalculatorApp()

root.call("wm", "iconphoto", root._w, tk.PhotoImage("calc.gif"))
root.mainloop()
