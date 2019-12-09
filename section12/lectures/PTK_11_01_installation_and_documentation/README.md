# Installation and Documentation

Install pyinstaller by running `pipenv install pyinstaller`.

Documentation is available here:

- [PyInstaller documentation](https://pyinstaller.readthedocs.io/en/stable/operating-mode.html)

## What it does

PyInstaller lets you build an executable that you can double-click and run without needing to install Python first.

Thus, it's great for sharing your applications with other people, especially non-developers.

When you run PyInstaller, it creates an executable for the Operating System that ran it. So if you run PyInstaller on Windows, it'll create a `.exe`. If you run it on Mac, it creates a `.app`.

To quote their official documentation:

> PyInstaller reads a Python script written by you. It analyzes your code to discover every other module and library your script needs in order to execute. Then it collects copies of all those files – including the active Python interpreter! – and puts them with your script in a single folder, or optionally in a single executable file.