import math

import pygame
from settings import Settings
from screen import Screen
from pygame import font
from time import sleep


class Drone:
    """A class to store all drone settings and parameters."""

    def __init__(self, rp):

        # Initialize destination coordinates.
        self.destination_y = None
        self.destination_x = None

        # Initialize 2D movement vector.
        self.movement_vector_y = None
        self.movement_vector_x = None

        self.screencl = Screen()

        # Initialize empty destination list to store waypoints.
        self.destination = []

        self.screen = self.screencl.screen
        self.settings = Settings()

        self.screen_rect = self.screencl.screen_rect

        # Load drone image and place it at the bottom of the screen.
        self.drone_img = pygame.image.load('drone_transparent.png')
        self.drone_rect = self.drone_img.get_rect()
        self.drone_rect.midbottom = self.screen_rect.midbottom

        # Assign drone coordinates to x, y.
        self.x = float(self.drone_rect.x)
        self.y = float(self.drone_rect.y)

        # Create empty lists for movement
        self.movement_vector = list()
        self.vector = list()

        # Create flag that will change to True if drone reaches the last waypoint.
        self.position_flag = False

        # Create the radius around the waypoint. When drone reaches the waypoint within the radius
        # autopilot proceeds to navigate to the next waypoint.
        self.radius = 10

        # Set drone speed.
        self.speed = 20

        # Set current waypoint to 0.
        self.waypoint_number = 0

        # I don't know what this does at the moment xD
        self.divider = list()

        # Run destination method which adds new waypoints to the destination list.
        self._destination()

        # Run method that calculates drone movement vector based on current position and waypoint position.
        self._vector_calculating(self.waypoint_number)

    def blitme(self):
        """Add drone image to screen every update."""
        self.screen.blit(self.drone_img, self.drone_rect)

        # Print current drone position (debugging feature).
        print("Drone position: ({}, {})".format(self.drone_rect.x, self.drone_rect.y))

    def drone_movement(self):
        """Move drone alongside current vector."""
        if not self.position_flag:

            # Change nominal position of the drone by the unit vector.
            self.x += self.vector[self.waypoint_number][0]
            self.y += self.vector[self.waypoint_number][1]

            # Assign nominal position to the drone's coordinates.
            self.drone_rect.x = self.x
            self.drone_rect.y = self.y

            # Check whether the drone reached the waypoint's radius.
            if abs(self.destination[self.waypoint_number][0] -
                   self.drone_rect.x) < self.radius and \
                    abs(self.destination[self.waypoint_number][1] - self.drone_rect.y) < self.radius:
                self.waypoint_number += 1
                if self.waypoint_number == len(self.destination):
                    self.position_flag = True
                else:
                    self._vector_calculating(self.waypoint_number)

    def _destination(self):
        """Add waypoints to the destination list."""
        self.destination.append((750, 500))
        self.destination.append((300, 600))
        self.destination.append((55, 55))
        self.destination.append((700, 100))

    def _vector_calculating(self, point_number):
        """Calculate vector movement based on current drone position and next waypoint."""

        # Create vector by subtracting current (X, Y) coordinates from waypoint's (X, Y) coordinates.
        # Add a vector to the vector list.
        self.vector.append([self.destination[point_number][0] - self.drone_rect.x,
                            self.destination[point_number][1] - self.drone_rect.y])

        # Measure vector length.
        temporary_speed = math.sqrt(math.pow(self.vector[point_number][0], 2) + math.pow(self.vector[point_number][1], 2))

        # Divide vector length by drone speed. self.divider variable will be used to calculate unit vector.
        # Unit vector is necessary to simulate drone movement by changing its position by unit vector.
        self.divider.append(temporary_speed / self.speed)

        # Swap vector (X, Y) coordinates for unit vector (X, Y) coordinates by dividing the vector coordinates
        # by the divider value.
        for i in range(len(self.vector)):
            for j in range(len(self.vector[i])):
                self.vector[i][j] /= self.divider[i]

        # Drone movement settings.
        # Assign current vector values to the movement vector.
        self.movement_vector_x = self.vector[0][0]
        self.movement_vector_y = self.vector[0][1]
