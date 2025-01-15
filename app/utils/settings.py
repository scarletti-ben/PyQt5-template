''' Docstring for .../app/utils/settings.py '''
# < ========================================================
# < Imports
# < ========================================================

import json

# < ========================================================
# < Settings Class
# < ========================================================

class Settings:

    TITLE: str = "PyQt5-template"
    ICON: str = "resources/icons/material-128x128.ico"
    X: int = 100
    Y: int = 100
    W: int = 720
    H: int = 480

    @classmethod
    def initialise(cls) -> None:
        """Initialise Settings and read from configuration file"""

        with open("app/utils/settings.json", 'r') as f:
            settings = json.load(f)
            cls.TITLE = settings.get("TITLE", cls.TITLE)
            cls.ICON = settings.get("ICON", cls.ICON)
            cls.X = settings.get("X", cls.X)
            cls.Y = settings.get("Y", cls.Y)
            cls.W = settings.get("W", cls.W)
            cls.H = settings.get("H", cls.H)