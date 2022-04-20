import pygame


class Food:
    def __init__(self):
        pygame.init()
        self.x = 5
        self.y = 4
        self.position = pygame.math.Vector2(self.x, self.y)

    def draw(self):
        food_rect = pygame.rect()