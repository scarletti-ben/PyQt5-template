''' Docstring for .../app/utils/settings.py '''
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