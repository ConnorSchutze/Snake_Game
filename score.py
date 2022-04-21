import pygame


class Score:
    def __init__(self, text_color = (0, 0, 0), score_x = 15, score_y = 15):
        pygame.init()
        self.text_color = text_color
        self.score_x = score_x
        self.score_y = score_y
        self.score_location = (self.score_x, self.score_y)
        self.font = pygame.font.Font(None, 25)
        self.screen = pygame.display.get_surface()
    
    def draw(self, snake):
        self.score = len(snake) - 3
        score_surface = self.font.render(str(self.score), True, self.text_color)
        score_rect = score_surface.get_rect(center = self.score_location)
        self.screen.blit(score_surface, score_rect)
