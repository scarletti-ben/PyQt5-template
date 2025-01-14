''' Docstring for .../app/utils/tools.py '''
# < ========================================================
# < Imports
# < ========================================================

import os
import logging

from .settings import Settings

from PyQt5.QtCore import Qt
from PyQt5.QtGui import (
    QPen, 
    QPixmap, 
    QColor, 
    QPainter,
    QIcon
)
from PyQt5.QtWidgets import (
    QWidget, 
    QApplication, 
    QMainWindow, 
    QGraphicsOpacityEffect, 
    QTableWidget
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

def window():
    """Property to return the QMainWindow of the current QApplication"""
    return get_main_window()

def set_opacity(widget: QWidget, opacity: float = 1.0) -> None:
    """Set opacity for a given widget"""
    effect = QGraphicsOpacityEffect()
    effect.setOpacity(opacity)
    widget.setGraphicsEffect(effect)

def rgba_to_hex(r: int, g: int, b: int, a: int = 255) -> str:
    """Convert RGBA value to a hex color code"""
    return f'#{r:02X}{g:02X}{b:02X}{a:02X}'

def center(window) -> None:
    """Center window in the center of the active display"""
    frameGm = window.frameGeometry()
    screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
    centerPoint = QApplication.desktop().screenGeometry(screen).center()
    frameGm.moveCenter(centerPoint)
    window.move(frameGm.topLeft())
    
def get_filename(extension: str = "") -> str:
    """Get filename from current date and time"""
    from datetime import datetime
    current_date: str = datetime.now().strftime("%Y-%m-%d")
    current_time: str = datetime.now().strftime("%H%M")
    return f"data_{current_date}_{current_time}" + extension

@staticmethod
def get_current_date_and_time() -> str:
    """Get the current date and time as a string"""
    from datetime import datetime
    current_date: str = datetime.now().strftime("%Y-%m-%d")
    current_time: str = datetime.now().strftime("%H:%M:%S")
    return f"[{current_date} | {current_time}]"

def clear_table(table: QTableWidget) -> None:
    """Clear data and rows from a QTableWidget"""
    table.clear() # < Not required but adds an extra layer of protection
    table.setRowCount(0)

def open_explorer_to_file(filepath):
    """Open a windows explorer window and highlight / select the specified filepath"""
    import subprocess
    explorer = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
    filepath = os.path.normpath(filepath)
    if os.path.isdir(filepath):
        subprocess.run([explorer, filepath])
    elif os.path.isfile(filepath):
        subprocess.run([explorer, '/select,', filepath])

def get_screen_size() -> tuple[int, int]:
    """Get the size of the current screen"""
    app = QApplication.instance()
    screen = app.primaryScreen()
    screen_geometry = screen.geometry()
    return screen_geometry.width(), screen_geometry.height()

def test() -> None:
    """Logs text, mainly used as a test function to check if a PyQt action is called correctly"""
    logging.info("tools.test function called")