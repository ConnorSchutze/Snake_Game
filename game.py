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
        move_update = pygame.USEREVENT
        pygame.time.set_timer(move_update, 150)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == move_update:
                    self.update()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.snake.direction = pygame.math.Vector2(0, -1)
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.snake.direction = pygame.math.Vector2(0, 1)
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.snake.direction = pygame.math.Vector2(-1, 0)
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.snake.direction = pygame.math.Vector2(1, 0)

            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.update()
            self.clock.tick(self.fps)
        
        pygame.quit()
        sys.exit()
    
    def draw(self):
        self.food.draw()
        self.snake.draw()

    def update(self):
        self.snake.movement()
        self.collisions()

    def collisions(self):
        if self.food.position == self.snake.body[0]:
            self.food.random_position()
            self.snake.new_snake_body()

if __name__ == '__main__':
    game = Game(400, 400)
    game.main()