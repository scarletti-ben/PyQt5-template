''' Docstring for .../app/widgets/custom_widget.py '''
# < ========================================================
# < Imports
# < ========================================================

from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import (
    QWidget, 
    QTextEdit,
)

# < ========================================================
# < CustomWidget Class
# < ========================================================

class CustomWidget(QTextEdit):
    def __init__(self, parent: QWidget = None, name: str = None) -> None:
        """Initialise a CustomWidget, with QTextEdit functionality"""
        super().__init__(parent)
        self.setObjectName(name)
        self.setText("This is a custom widget")
        self.moveCursor(QTextCursor.End)