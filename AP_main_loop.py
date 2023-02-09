import sys
import pygame
from settings import Settings
from drone import Drone
from time import sleep
from screen import Screen


class RewPilot:
    """Overall class to manage autopilot behavior."""

    def __init__(self):
        pygame.init()

        # import Screen class
        self.screencl = Screen()

        # import Settings class and assign screen parameters
        self.settings = Settings()
        self.screen = self.screencl

        self.screen_rect = self.screencl.screen_rect
        pygame.display.set_caption("RewPilot")

        self.bg_color = (230, 230, 230)

        # import Drone class
        self.drone = Drone(self)

    def run_ap(self):
        """Start the main loop for the autopilot"""
        while True:
            # Check if user wants to quit the simulator.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Change screen's background color.
            self.screencl.screen.fill(self.bg_color)

            # Update drone coordinates and image.
            self.drone.drone_movement()
            self.drone.blitme()

            pygame.display.flip()
            sleep(0.05)


if __name__ == '__main__':
    ap = RewPilot()
    ap.run_ap()
