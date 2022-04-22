"""File: food.py.

Team NO: 5
Author: Connor Schutze
Description: Generating food onto the screen in random places.
"""

import pygame
import random
from pygame.math import Vector2


class Food:
    """Create a food object for the snake to eat."""

    def __init__(self, cell_size, cell_width, cell_height):
        """Create the food attributes.

        Get the amount of cells, sizes, and display surface.
        As well as set the position of the original food placement.
        """
        pygame.init()
        self.cell_size = cell_size
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.apple = pygame.image.load("Images/apple.png").convert_alpha()
        self.apple = pygame.transform.scale(self.apple, (cell_size, cell_size))
        self.screen = pygame.display.get_surface()

        self.random_position()

    def draw(self):
        """Draw the fruit onto the display surface."""
        food_rect = pygame.Rect(int(self.position.x * self.cell_size),
                                int(self.position.y * self.cell_size),
                                self.cell_size, self.cell_size)
        self.screen.blit(self.apple, food_rect)

    def random_position(self):
        """Find one random cell on screen for the food to spawn."""
        self.x = random.randint(0, self.cell_width-1)
        self.y = random.randint(self.cell_width-self.cell_height,
                                self.cell_height-1)
        self.position = Vector2(self.x, self.y)
