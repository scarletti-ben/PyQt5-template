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
    X: int = 100
    Y: int = 100
    W: int = 720
    H: int = 480

    @classmethod
    def initialise(cls) -> None:
        """Initialise Settings and read from configuration file"""

        with open("app/utils/settings.json", 'r') as f:
            settings = json.load(f)
            cls.TITLE = settings.get("TITLE", "PyQt5-template")
            cls.X = settings.get("X", 100)
            cls.Y = settings.get("Y", 100)
            cls.W = settings.get("W", 720)
            cls.H = settings.get("H", 480)