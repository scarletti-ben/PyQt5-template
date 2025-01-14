''' Docstring for .../app/widgets/status_bar.py '''
# < ========================================================
# < Imports
# < ========================================================

from PyQt5.QtWidgets import (
    QWidget, 
    QStatusBar
)

# < ========================================================
# < StatusBar Widget Class
# < ========================================================

class StatusBar(QStatusBar):
    def __init__(self, parent: QWidget = None) -> None:
        """Initialise a StatusBar widget"""
        super().__init__(parent)
        self.showMessage("Default status message")