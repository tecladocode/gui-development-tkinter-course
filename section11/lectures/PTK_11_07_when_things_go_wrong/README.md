# When things go wrong

PyInstaller has a lengthy section of their documentation detailing what to do when things go wrong: https://pyinstaller.readthedocs.io/en/stable/when-things-go-wrong.html

In addition to that, I'd like to give you some practical tips.

## Keeping the Windows console when an error happens

By default, the Windows console will automatically close when the application crashes. This can make it really difficult to see an error that's printed out there.

The first time you encounter an error, you should surround your entire code with a try-except block. In there, print the traceback and also include an `input()` statement so that the Windows console does not close until you enter something (to satisfy the `input()` function).

Like this:

```
try:
    root = tk.Tk()
    root.title("Snake")
    root.resizable(False, False)

    board = Snake()
    board.pack()


    root.mainloop()
except:
    import traceback
    traceback.print_exc()
    input("Press Enter to end...")
```