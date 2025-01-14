# WORK IN PROGRESS

In its current state, this `README.md` is a work in progress and the template is non-functional.

# PyQt Template

### Project Template
```
00 PyQt5-template/
01 ├── app/
02 │   ├── utils/
03 │   │   ├── __init__.py
04 │   │   ├── settings.py
05 │   │   └── tools.py
06 │   ├── widgets/
07 │   │   ├── __init__.py
08 │   │   └── menu.py
09 │   ├── __init__.py
10 │   └── widget.py
11 ├── resources/
12 │   ├── icons/
13 │   │   └── icon.png
14 │   └── fonts/
15 │       └── font.ttf
16 ├── .gitignore
17 ├── LICENSE
18 ├── main.py
19 ├── README.md
20 └── requirements.txt
```

# Miscellaneous
- Add logging
- No logging, check console for print statements
- Without `Qt Designer`
- `app` at line `01` is a top-level package
- Settings are initialised early, and therefore accessable by any future modules
- Extensible
- Modular
- You can find `PyQt5` on `PyPi` via this [link](https://pypi.org/project/PyQt5/)
- Containers need central_widgets and layouts
- Suggestions: setObjectName => Works similar to id="" in HTML so that you can search for an element to change without a direct reference to it

```python
class Menu(QMenuBar):
    def __init__(self, parent: QWidget = None) -> None:
        """Initialise a Menu object"""
        super().__init__(parent)
```

- Super and parent are essentially ensuring the widget goes into the layout of the parent

```
The QMainWindow is a special widget which comes bundled with a bunch of built-in capabilities, such as the dock widgets, toolbars, statusbars and menus. These are all handled through built-in layouts on the main window.

Because of this you can’t override the layout on a QMainWindow object, like you can for other widgets (if you did, none of these things would work).

The setCentralWidget sets a widget into the middle of the window layout, in a region set aside for the window content.

If you want to set a layout on the content in the main window, you can create a container widget using QWidget and apply the layout to that.
```

You can use QWidget instead of QMainWindow but it won't have toolbar / statusbar etc functionality
