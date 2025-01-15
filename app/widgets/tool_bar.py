''' Docstring for .../app/widgets/tool_bar.py '''
# < ========================================================
# < Imports
# < ========================================================

from PyQt5.QtWidgets import (
    QWidget, 
    QToolBar
)

# < ========================================================
# < ToolBar Widget Class
# < ========================================================

class ToolBar(QToolBar):
    def __init__(self, title: str, parent: QWidget = None) -> None:
        """Initialise a ToolBar widget"""
        super().__init__(title, parent)