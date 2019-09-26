# ttk Style themes

We can access the style database by creating an instance of `ttk.Style()`:

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style(root)

...
```

This allows us to access and customize styles for the Tk application passed, in this case `root`.

## Themes

Every Operating System comes with themes. A theme is a collection of styles for Tkinter widgets, so that if you enable one theme, those styles will be applied.

You can see which themes are available like so:

```python
style = ttk.Style(root)
print(style.theme_names())
```

And you can change the theme like so:

```python
style = ttk.Style(root)
style.theme_use("classic")  # Use a theme available in your system
```