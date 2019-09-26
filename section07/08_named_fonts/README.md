# Named fonts

Read the Tk Docs for more: https://tkdocs.com/tutorial/fonts.html

A couple of things are important to know:

> The "family" specifies the font name; the names Courier, Times, and Helvetica are guaranteed to be supported (and mapped to an appropriate monospaced, serif, or sans-serif font).

## Create your own font

Creating your own font is easy enough. It gets stored in a variable and can be reused anywhere where our known font tuple could be passed:

```python
import tkinter.font as font

warningLabelFont = font.Font(family="Helvetica", size=14, weight="bold")
```

## Re-use the default font

If you do this:

```python
import tkinter.font as font

warningLabelFont = font.nametofont("TkDefaultFont")
warningLabelFont.configure(size=15)
```

You'll have problems, because the `warningLabelFont` _is_ the default font. That means that all widgets which use the default font will change size.

Instead, `.copy()` the font to only use it in certain widgets:

```python
import tkinter.font as font

warningLabelFont = font.nametofont("TkDefaultFont").copy()
warningLabelFont.configure(size=15)
```