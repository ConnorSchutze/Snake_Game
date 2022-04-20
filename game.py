import pygame
import sys
from snake import Snake
from food import Food


class Game:
    """Creation of the snake game."""
    def __init__(self, screen_width, screen_height, cell_size, cell_width, cell_height):
        """Creation of the screen and game attributes."""
        pygame.init()
        self.cell_size = cell_size
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()

        self.fps = 60
        self.running = True

        self.snake = Snake(self.cell_size)
        self.food = Food(self.cell_size, self.cell_width, self.cell_height)
    
    def main(self):
        """Main game loop."""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))
            self.snake.draw()
            self.food.draw()
            # ------ Temporary code, top box -----
            box_rect = pygame.Rect(0, 0, self.screen_width, 80)
            pygame.draw.rect(self.screen, (0, 255, 255), box_rect)
            # ------ Temporary code, top box -----
            pygame.display.update()
            self.clock.tick(self.fps)
        
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    game = Game(400, 400)
    game.main()