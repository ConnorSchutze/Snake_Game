import pygame


class Score:
    def __init__(self, cell_size, text_color = (0, 0, 0), score_x = 40, score_y = 20):
        pygame.init()
        self.text_color = text_color
        self.apple = pygame.image.load("Images/apple.png").convert_alpha()
        self.apple = pygame.transform.scale(self.apple, (cell_size, cell_size))
        self.score_x = score_x
        self.score_y = score_y
        self.score_location = (self.score_x, self.score_y)
        self.font = pygame.font.Font(None, 25)
        self.screen = pygame.display.get_surface()
        self.fg_color = (255, 255, 255)
        self.bg_color = (0, 0, 0)
    
    def draw(self, snake):
        self.score = len(snake) - 3
        score_surface = self.font.render(str(self.score), True, self.text_color)
        score_rect = score_surface.get_rect(center = self.score_location)
        apple_rect = self.apple.get_rect(midright = (score_rect.x, score_rect.centery))
        fg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 6,apple_rect.height)

        pygame.draw.rect(self.screen, self.fg_color, fg_rect)
        self.screen.blit(score_surface, score_rect)
        self.screen.blit(self.apple, apple_rect)
        pygame.draw.rect(self.screen, self.bg_color, fg_rect, 1)
