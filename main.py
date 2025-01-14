''' Docstring for .../main.py '''
# < ========================================================
# < Imports
# < ========================================================

import sys
from PyQt5.QtWidgets import QApplication
from app.main_window import MainWindow
from app.utils.settings import Settings

# < ========================================================
# < Execution
# < ========================================================

app = QApplication(sys.argv) # < Initialise the PyQt5 core and pass system arguments
Settings.initialise() # < Initialise settings and load configuration files
window = MainWindow() # < Initialise the window, including its layout and widgets
window.show()  # < Display the window on the screen
sys.exit(app.exec()) # < Start the event loop and exit when the window is closed