import pygame
import sys
from snake import Snake


class Game:
    """Creation of the snake game."""
    def __init__(self, screen_width, screen_height, fps):
        """Creation of the screen and game attributes."""
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()

        self.fps = fps
        self.running = True
    
    def main(self):
        """Main game loop."""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))
            pygame.display.update()
            self.clock.tick(self.fps)


if __name__ == '__main__':
    game = Game(400, 400)
    game.main(60)

    pygame.quit()
    sys.exit()