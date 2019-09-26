# High DPI Settings

To enable High DPI compatibility in Windows 10, you normally just have to add this:

```python
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
```

However if you still run into scaling problems, check out [this StackOverflow topic](https://stackoverflow.com/questions/41315873/attempting-to-resolve-blurred-tkinter-text-scaling-on-windows-10-high-dpi-disp).