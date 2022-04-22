import pygame
from snake import Snake
from food import Food
from score import Score


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

        self.game_text_color = (255, 255, 255)
        self.game_font = pygame.font.Font(None, 25)
        self.game_text = self.game_font.render("Restart (r) Quit (q)", True, self.game_text_color)
        self.game_text_rect = self.game_text.get_rect(center = (150, 20))

        self.fps = 60
        self.running = True

    def main(self):
        """Main game loop."""
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()

        self.snake = Snake(self.cell_size)
        self.food = Food(self.cell_size, self.cell_width, self.cell_height)
        self.score = Score(self.cell_size)

        self.game_started = False
        self.direction_choosen = False
        move_update = pygame.USEREVENT
        pygame.time.set_timer(move_update, 150)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == move_update:
                    self.update()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.snake.reset()
                    if event.key == pygame.K_q:
                        self.running = False
                if event.type == pygame.KEYDOWN and self.direction_choosen == False:
                    self.game_started = True
                    self.direction_choosen = True
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        if self.snake.direction.y != 1:
                            self.snake.direction = pygame.math.Vector2(0, -1)
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        if self.snake.direction.y != -1:
                            self.snake.direction = pygame.math.Vector2(0, 1)
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        if self.snake.direction.x != 1:
                            self.snake.direction = pygame.math.Vector2(-1, 0)
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        if self.snake.direction.x != -1:
                            self.snake.direction = pygame.math.Vector2(1, 0)

            self.screen.fill((0, 255, 150))
            self.draw()
            pygame.display.update()
            self.clock.tick(self.fps)
        
        pygame.quit()
    
    def draw(self):
        """Draw snake and food onto the display surface."""
        self.background()
        self.food.draw()
        self.snake.draw()
        self.score.draw(self.snake.body)

    def update(self):
        """Updating the screen for movement and collisions."""
        self.direction_choosen = False
        self.snake.movement(self.game_started)
        self.collisions()
        self.die()

    def collisions(self):
        """Detect the collisions between snake and food."""
        if self.food.position == self.snake.body[0]:
            self.food.random_position()
            self.snake.new_snake_body()
            self.snake.play_eat_sound()
            self.score.highest_score()
        
        for snake_body in self.snake.body[1:]:
            if snake_body == self.food.position:
                self.food.random_position()

    def die(self):
        """Detect whether the snake died or not."""
        if not 0 <= self.snake.body[0].x <= self.cell_width or not 2 <= self.snake.body[0].y <= self.cell_height:
            self.game_over()
        
        for snake_body in self.snake.body[1:]:
            if snake_body == self.snake.body[0] and self.game_started:
                self.game_over()
    
    def game_over(self):
        """When the snake dies, displays Game Over text and options."""
        self.snake.reset()
        self.game_started = False
        while self.game_started == False:
            self.screen.blit(self.game_text, self.game_text_rect)

    def background(self):
        color_one = (0, 255, 0)

        for row in range(self.cell_height):
            row += 2
            if row % 2 == 0:
                for column in range(self.cell_width):
                    if column % 2 == 0:
                        checker1_rect = pygame.Rect(column * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                        pygame.draw.rect(self.screen, color_one, checker1_rect)
            else:
                for column in range(self.cell_width):
                    if column % 2 != 0:
                        checker1_rect = pygame.Rect(column * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                        pygame.draw.rect(self.screen, color_one, checker1_rect)


if __name__ == '__main__':
    game = Game((17*30),(17*30), 30, 17, 15)
    game.main()
