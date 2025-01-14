''' Docstring for .../app/main_window.py '''
# < ========================================================
# < Imports
# < ========================================================

from PyQt5.QtWidgets import (
    QApplication,
    QWidget, 
    QMainWindow, 
    QVBoxLayout,
    QShortcut,
    QAction
)
from PyQt5.QtGui import (
    QIcon,
    QKeySequence
)

from .utils.settings import Settings
from .widgets.menu_bar import MenuBar
from .widgets.status_bar import StatusBar
from .widgets.custom_widget import CustomWidget

# < ========================================================
# < MainWindow Class
# < ========================================================

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        """Initialise the MainWindow"""
        super().__init__()
        self.setWindowTitle(Settings.TITLE)
        self.setWindowIcon(QIcon())
        self.setGeometry(Settings.X, Settings.Y, Settings.W, Settings.H)
        self.initialise_central_widget()
        self.setMenuBar(MenuBar(self))
        self.setStatusBar(StatusBar(self))
        self.center()
        self.initialise_extras()

    def center(self) -> None:
        """Center MainWindow within the active display"""
        rectangle = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        rectangle.moveCenter(centerPoint)
        self.move(rectangle.topLeft())

    def initialise_central_widget(self) -> None:
        """Initialise central widget and layout for MainWindow"""
        self.central_widget = QWidget(self)
        self.central_layout = QVBoxLayout(self.central_widget)
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)

    def add_widget(self, widget: QWidget) -> None:
        """Add widget to the central layout, and set parent to MainWindow"""
        self.central_layout.addWidget(widget)

    def add_shortcut(self, sequence: str, func: callable) -> None:
        """Add a keyboard shortcut to the MainWindow"""
        shortcut = QShortcut(QKeySequence(sequence), self)
        shortcut.activated.connect(func)

    # - ==============================================
    # - Customisable Methods
    # - ==============================================

    def initialise_extras(self) -> None:
        """Example of messy MainWindow code separated from the rest"""

        def test(*args):
            """Test function"""
            print(f"Test function called with args: {args}")

        # ! ==============================================
        # ! Add a Widget to MainWindow
        # ! ==============================================
        
        widget = CustomWidget(self, "name")
        self.add_widget(widget)

        # ! ==============================================
        # ! Add a Keyboard Shortcut
        # ! ==============================================
    
        self.add_shortcut("Ctrl+O", test)

        # ! ==============================================
        # ! Add to Menu (Can be done in menu.py)
        # ! ==============================================

        menu = self.menuBar()
        menu.help_menu = menu.addMenu("&Help")
        action = QAction(QIcon(), "&Information", menu)
        action.setStatusTip("'Information' button status message")
        action.triggered.connect(test)
        menu.help_menu.addAction(action)