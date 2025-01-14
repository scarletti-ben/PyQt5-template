''' Docstring for .../app/window.py '''
# < ========================================================
# < Imports
# < ========================================================

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, 
    QApplication, 
    QMainWindow, 
    QHBoxLayout,
    QTextEdit
)

from .utils.settings import Settings
from .widgets.menu import Menu

# < ========================================================
# < Window Class
# < ========================================================

class Window(QMainWindow):
    def __init__(self) -> None:
        """Initialise the Window object"""