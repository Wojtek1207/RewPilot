# from destination import Destination


class Settings:
    """A class to store all autopilot settings."""
    def __init__(self):

        # Screen settings.
        self.height = 720
        self.width = 1080

        # Drone movement settings.
        self.movement_vector_x = 200
        self.movement_vector_y = 200
