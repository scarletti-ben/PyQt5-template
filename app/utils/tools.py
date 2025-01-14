''' Docstring for .../app/utils/tools.py '''
# < ========================================================
# < Imports
# < ========================================================

from PyQt5.QtCore import Qt
from PyQt5.QtGui import (
    QPen, 
    QPixmap, 
    QColor, 
    QPainter,
    QIcon
)
from PyQt5.QtWidgets import (
    QApplication, 
    QMainWindow
)

# < ========================================================
# < Functionality
# < ========================================================
    
def get_default_icon():
    """Get default icon from saved bitmap"""
    bitmap = [
        "11111111",
        "11111111",
        "11000011",
        "11000011",
        "11000011",
        "11000011",
        "11111111",
        "11111111"
        ]
    size = len(bitmap)
    pixmap = QPixmap(size, size)
    pixmap.fill(QColor(Qt.transparent))
    painter = QPainter(pixmap)
    painter.setPen(QPen(QColor(255, 255, 255)))
    for y in range(size):
        for x in range(size):
            if bitmap[y][x] == '1':
                painter.drawPoint(x, y)
    painter.end()
    return QIcon(pixmap)

def get_main_window() -> QMainWindow:
    """Function to find the QMainWindow of the current QApplication"""
    app = QApplication.instance()
    for widget in app.topLevelWidgets():
        if isinstance(widget, QMainWindow):
            return widget