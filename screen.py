import pygame

from settings import Settings


class Screen:
    """A class to manage screen behavior."""
    def __init__(self):
        self.settings = Settings()
        self.height = self.settings.height
        self.width = self.settings.width

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen_rect = self.screen.get_rect()

        self.bg_color = (230, 230, 230)

        self.screen.fill(self.bg_color)

