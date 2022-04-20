import pygame
import random
from pygame.math import Vector2


class Food:
    def __init__(self, cell_size, cell_width, cell_height):
        pygame.init()
        self.cell_size = cell_size
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.color = (255, 0, 0)
        self.screen = pygame.display.get_surface()

        # Food position
        self.x = random.randint(0, self.cell_width-1)
        self.y = random.randint(2, self.cell_height-1)
        self.position = Vector2(self.x, self.y)

    def draw(self):
        """Draw the fruit onto the display surface."""
        food_rect = pygame.Rect(int(self.position.x * self.cell_size), 
                                int(self.position.y * self.cell_size), 
                                self.cell_size, self.cell_size)
        pygame.draw.rect(self.screen, self.color, food_rect)