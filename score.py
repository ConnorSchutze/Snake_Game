"""File: score.py.

Team NO: 5
Author: Connor Schutze and Zac Ohran
Description: Score class, keeps score and high score.
"""

import pygame


class Score:
    """Create the score and highest score for the snake game."""

    def __init__(self, cell_size, text_color=(0, 0, 0), score_x=40,
                 score_y=20):
        """Create the attributes for the text of the score."""
        pygame.init()
        self.text_color = text_color
        self.apple = pygame.image.load("Images/apple.png").convert_alpha()
        self.apple = pygame.transform.scale(self.apple, (cell_size, cell_size))
        self.golden_apple = pygame.image.load("Images/golden_apple.png") \
            .convert_alpha()
        self.golden_apple = pygame.transform.scale(self.golden_apple,
                                                   (cell_size,
                                                    cell_size))
        self.score_x = score_x
        self.score_y = score_y
        self.score_location = (self.score_x, self.score_y)
        self.high_score = 0
        self.font = pygame.font.Font(None, 25)
        self.screen = pygame.display.get_surface()
        self.fg_color = (255, 255, 255)
        self.bg_color = (0, 0, 0)

    def draw(self, snake):
        """Draw the score and highest score onto the screen."""
        self.score = len(snake) - 3
        score_surface = self.font.render(str(self.score), True,
                                         self.text_color)
        high_surface = self.font.render(str(self.high_score), True,
                                        self.text_color)
        score_rect = score_surface.get_rect(center=self.score_location)
        high_rect = score_surface.get_rect(topleft=(score_rect.x + 75,
                                                    score_rect.y))
        apple_rect = self.apple.get_rect(midright=(score_rect.x,
                                                   score_rect.centery))
        golden_rect = self.golden_apple.get_rect(midright=(high_rect.x,
                                                           high_rect.centery))
        fg_rect = pygame.Rect(apple_rect.left, apple_rect.top,
                              apple_rect.width + score_rect.width + 6,
                              apple_rect.height)
        fg_high_rect = pygame.Rect(golden_rect.left, golden_rect.top,
                                   golden_rect.width + high_rect.width + 6,
                                   golden_rect.height)

        pygame.draw.rect(self.screen, self.fg_color, fg_rect)
        pygame.draw.rect(self.screen, self.fg_color, fg_high_rect)
        self.screen.blit(score_surface, score_rect)
        self.screen.blit(high_surface, high_rect)
        self.screen.blit(self.apple, apple_rect)
        self.screen.blit(self.golden_apple, golden_rect)
        pygame.draw.rect(self.screen, self.bg_color, fg_rect, 1)
        pygame.draw.rect(self.screen, self.bg_color, fg_high_rect, 1)

    def highest_score(self):
        """Update the high score for the screen."""
        if self.score >= self.high_score:
            self.high_score = self.score + 1
