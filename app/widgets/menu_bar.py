''' Docstring for .../app/widgets/menu_bar.py '''
# < ========================================================
# < Imports
# < ========================================================

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QWidget, 
    QMenuBar,
    QAction
)

# < ========================================================
# < MenuBar Widget Class
# < ========================================================

class MenuBar(QMenuBar):
    def __init__(self, parent: QWidget = None) -> None:
        """Initialise a MenuBar widget"""
        super().__init__(parent)
        self.initialise_menu()

    def initialise_menu(self) -> None:
        """Initialise all Menu dropdowns"""
        self.file_menu = self.addMenu("&File")
        action = QAction(QIcon(), "&Open", self)
        action.setStatusTip("'Open' button status message")
        action.triggered.connect(lambda: None)
        self.file_menu.addAction(action)