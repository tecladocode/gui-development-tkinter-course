# Changing ttk.Entry field font with ttk.Style

The gist of is, you can't. There might be a bug in the Tk engine which means that applying a `ttk.Style()` which uses the `font=` argument on a `ttk.Entry` results in the font change not being shown on the entry field.

Therefore, for `ttk.Entry` fields you must pass the `font=` argument directly to the constructor.

In other words, this won't work on entry fields. Or at least, the font will continue being the default font:

```python
style = ttk.Style()
style.configure("LargeEntry.TEntry", font=("Segoe UI", 15))
entry = ttk.Entry(root, style="LargeEntry.TEntry")
entry.pack()
```

However, this _will_ change the font:

```python
entry = ttk.Entry(root, font=("Segoe UI", 15))
entry.pack()
```

## Using the global entry font

The next lecture in this course talks how to use the global entry font, and how that can greatly simplify your font-setting on `ttk.Entry` fields. However, it is partially limited in that it will change the styling for _all_ entry fields:

```python
import tkinter.font as font

...

font.nametofont("TkEntryFont").configure(size=15)

...

entry = ttk.Entry(root)  # The font is 15 pixels
entry.pack()
```

## Tkinter specially named fonts

Font name          | Description
-------------------|----------------------------------------------
TkDefaultFont      | Default for items not otherwise specified.
TkTextFont         | Used for entry widgets, listboxes, etc.
TkFixedFont        | A standard fixed-width font.
TkMenuFont         | The font used for menu items.
TkHeadingFont      | Font for column headings in lists and tables.
TkCaptionFont      | A font for window and dialog caption bars.
TkSmallCaptionFont | A smaller caption font for tool dialogs.
TkIconFont         | A font for icon captions.
TkTooltipFont      | A font for tooltips.

## Using named fonts

The most flexible approach is to define custom fonts (that can inherit from `TkEntryFont` or `TkDefaultFont`), and then manually pass them to each entry field. We also look at that in this course, in the lecture after the next.