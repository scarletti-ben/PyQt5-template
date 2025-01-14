''' Docstring for .../app/widgets/menu_bar.py '''
# < ========================================================
# < Imports
# < ========================================================

from PyQt5.QtWidgets import (
    QWidget, 
    QMenuBar
)

# < ========================================================
# < MenuBar Widget Class
# < ========================================================

class MenuBar(QMenuBar):
    def __init__(self, parent: QWidget = None) -> None:
        """Initialise a MenuBar widget"""
        super().__init__(parent)