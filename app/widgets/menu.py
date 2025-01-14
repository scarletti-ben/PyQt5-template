''' Docstring for .../app/window.py '''
# < ========================================================
# < Imports
# < ========================================================

from PyQt5.QtWidgets import (
    QWidget, 
    QMenuBar
)

# < ========================================================
# < Menu Class
# < ========================================================

class Menu(QMenuBar):
    def __init__(self, parent: QWidget = None) -> None:
        """Initialise a Menu object"""
        super().__init__(parent)