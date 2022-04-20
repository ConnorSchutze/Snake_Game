import pygame
import sys
from snake import Snake


class Game:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()

        self.running = True
    
    def main(self, fps):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))
            pygame.display.update()
            self.clock.tick(fps)


if __name__ == '__main__':
    game = Game(400, 400)
    game.main(60)

    pygame.quit()
    sys.exit()