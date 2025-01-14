# PyQt Template
- You can find `PyQt5` on `PyPi` via this [link](https://pypi.org/project/PyQt5/)

### Overview
This template repository contains the skeleton of a `PyQt5` application, written in `Python`. With the current directory structure it is easy to add new custom widgets to the `widgets` folder, and alter the widgets displayed in the app by editing `main_window.py`.

### Entry Point
The entry point of the app is `main.py`, it initialises the `PyQt5` application, loads configuration settings, creates the `MainWindow` and starts the application.
```python
# Excerpt from main.py

app = QApplication(sys.argv) # < Initialise the PyQt5 core and pass system arguments
Settings.initialise() # < Initialise settings and load configuration files
window = MainWindow() # < Initialise the window, including its layout and widgets
window.show()  # < Display the window on the screen
sys.exit(app.exec()) # < Start the event loop and exit when the window is closed
```

### Adding and Changing Functionality of the Application
Unless doing a major overhaul of the project, you can get a lot of mileage out of editing `main_window.py`

Currently, the method `initialise_extras` on the `MainWindow` class has been used to separate custom code from the more essential initialisation. Starting there might be easiest.
```python
def initialise_extras(self) -> None:
    """Example of messy MainWindow code separated from the rest"""
```
In practice you can edit any function, method, class or module in the project in any way to add or change functionality!

# Miscellaneous
- Project is for manual tweaking of widgets and layouts, without the use of `Qt Designer`
- No logging is currently enabled for this simple project, occasional `print` statements have been used instead
- `settings.py` is used to read `settings.json` and load relevant settings for the main application, no functionality has yet been added for altering settings during runtime

### Project Structure
```
00 PyQt5-template/
01 ├── app/
02 │   ├── utils/
03 │   │   ├── __init__.py
04 │   │   ├── settings.py
05 │   │   └── tools.py
06 │   ├── widgets/
07 │   │   ├── __init__.py
08 │   │   ├── custom_widget.py
09 │   │   ├── menu_bar.py
10 │   │   └── status_bar.py
11 │   ├── __init__.py
12 │   └── main_window.py
13 ├── resources/
14 │   ├── fonts/
15 │   │   └── font.ttf
16 │   └── icons/
17 │       └── icon.png
18 ├── .gitignore
19 ├── LICENSE
20 ├── main.py
21 ├── README.md
22 └── requirements.txt
```