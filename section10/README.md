# Packaging and Distributing Python Executables

If you want to distribute your Tkinter applications, we recommend using PyInstaller.

- [Their website](http://www.pyinstaller.org/);
- [Their documentation](https://pyinstaller.readthedocs.io/en/stable/);
- [Their GitHub](https://github.com/pyinstaller/pyinstaller);
- [Their FAQ](https://github.com/pyinstaller/pyinstaller/wiki/FAQ).

The gist of it is: PyInstaller will let you turn your Python applications into an executable for the platform that makes the executable.

That means that, if you build your application on Windows, it'll produce a `.exe`. If you run it on Mac, it'll produce a `.app`, and so on.

To install PyInstaller, just `pip install pyinstaller`. Make sure to activate your virtual environment first.

Then, you can build your Tkinter applications and turn them into executables with this command:

```
pyinstaller app.py --onefile
```

This will produce two folders: `build` and `dist`. Inside the latter, you'll find your executable. You can share and distribute this with other people, even if they don't have Python in their system!