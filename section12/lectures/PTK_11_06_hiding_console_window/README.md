# Hiding the console window

By default, a console window is created for you.

If you want to not do that, use a `.pyw` extension instead of `.py` for your app, before running PyInstaller.

Do note that doing this will prevent you from seeing errors shown in the console!

## The `--windowed` option

Alternatively, and arguably a better option, is to provide the `--windowed` option as well as `--onefile` or `--onefolder`.

If there is an error while launching the application when using windowed mode, you'll get an error modal popup on your operating system.