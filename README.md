# PyQt Template

### Overview
This template repository contains the skeleton of a `PyQt5` application, written in `Python`. With the current directory structure it is easy to add new custom widgets to the `widgets` folder, and alter the widgets displayed in the app by editing `main_window.py`.

### Installing Repository and Dependencies
- Ensure you have `git` installed
- Ensure you have `python` installed, the recommended version is `Python 3.12.1`
- Clone the repository via `git clone https://github.com/scarletti-ben/PyQt5-template`
- Enter the repository via `cd .\PyQt5-template\`
- Set up the virtual environment
  -  Initialise the virtual environment via `python -m venv venv`
  -  Activate the virtual environment via `.\venv\Scripts\activate`
- Install required packages via `pip install -r requirements.txt`

### Entry Point
The entry point of the app is `main.py`, you can run the application from the virtual environment via `python main.py`.

The `main.py` script initialises the `PyQt5` application, loads configuration settings, creates the `MainWindow` and starts the application.
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
- The project does not make use of `Qt Designer`
- The `logging` module is not currently used in this project, occasional `print` statements have been used instead
- `settings.py` is used to read `settings.json` and load relevant settings for the main application, no functionality has yet been added for altering settings during runtime
- `PyQt5-template` installs and uses `PyQt5`, you can read about it on `PyPi` via this [link](https://pypi.org/project/PyQt5/)

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
10 │   │   ├── status_bar.py
11 │   │   └── tool_bar.py
12 │   ├── __init__.py
13 │   ├── main_window.py
14 │   └── settings.json
15 ├── resources/
16 │   ├── fonts/
17 │   │   └── ...
18 │   └── icons/
19 │       └── ...
20 ├── .gitignore
21 ├── LICENSE
22 ├── main.py
23 ├── README.md
24 └── requirements.txt
```

### Installing Repository and Dependences / Running `main.py` in a Virtual Environment (GIF)
![animation](https://github.com/user-attachments/assets/a9394f03-7d7b-4b9d-b646-38db22aa9328)