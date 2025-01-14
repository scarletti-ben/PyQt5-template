''' Docstring for .../main.py '''
# < ========================================================
# < Imports
# < ========================================================

import sys
from PyQt5.QtWidgets import QApplication
from app.window import Window
from app.utils.settings import Settings

# < ========================================================
# < Execution
# < ========================================================

app = QApplication(sys.argv)
Settings.initialise()
window = Window()
window.show()
sys.exit(app.exec())