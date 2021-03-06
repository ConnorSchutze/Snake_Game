"""File: game.py.

Team NO: 5
Author: Connor Schutze and Zac Ohran
Description: Creates the snake, food, score, and background objects.
Runs the actual snake game and all of the functions with it.
"""

import pygame
from snake import Snake
from food import Food
from score import Score


class Game:
    """Creation of the snake game."""

    def __init__(self, screen_width, screen_height, cell_size, cell_width,
                 cell_height):
        """Creation of the screen, text, text boxes, and game attributes."""
        pygame.init()

        # Screen and cell creation
        self.cell_size = cell_size
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Text and text boxes
        self.game_text_color = (21, 61, 28)
        self.game_over_color = (255, 0, 0)
        self.fg_color = (255, 255, 255)
        self.bg_color = (0, 0, 0)
        self.game_font = pygame.font.Font(None, 25)
        self.game_over_font = pygame.font.Font(None, 50)
        self.game_text = self.game_font.render("Restart (r) Quit (q)", True,
                                               self.game_text_color)
        self.game_over_text = self.game_over_font.render("GAME OVER", True,
                                                         self.game_over_color)
        self.game_text_rect = self.game_text.get_rect(
                                                    center=(screen_width-100,
                                                            20))
        self.game_over_rect = self.game_over_text.get_rect(
                                                          center=(
                                                            screen_width/2,
                                                            screen_height/2))
        self.fg_rect = pygame.Rect(self.game_over_rect.left - 10,
                                   self.game_over_rect.top - 10,
                                   self.game_over_rect.width + 20,
                                   self.game_over_rect.height + 20)

        # Game attributes
        self.fps = 60
        self.running = True
        self.dead = False

    def main(self):
        """Run the actual game and game loop."""
        self.screen = pygame.display.set_mode((self.screen_width,
                                               self.screen_height))
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
                        self.dead = False
                    if event.key == pygame.K_q:
                        self.running = False
                if event.type == pygame.KEYDOWN and \
                   self.direction_choosen is False:
                    self.game_started = True
                    self.dead = False
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
        self.screen.blit(self.game_text, self.game_text_rect)

        if self.dead:
            pygame.draw.rect(self.screen, self.fg_color, self.fg_rect)
            self.screen.blit(self.game_over_text, self.game_over_rect)
            pygame.draw.rect(self.screen, self.bg_color, self.fg_rect, 1)

    def update(self):
        """Update the screen for movement, collisions, and snake death."""
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
        if not 0 <= self.snake.body[0].x <= self.cell_width or \
           not 2 <= self.snake.body[0].y <= self.cell_height:
            self.game_over()

        for snake_body in self.snake.body[1:]:
            if snake_body == self.snake.body[0] and self.game_started:
                self.game_over()

    def game_over(self):
        """When the snake dies, displays Game Over text and options."""
        self.snake.reset()
        self.dead = True

    def background(self):
        """Create the checkered background where the snake can move."""
        color_one = (0, 255, 0)

        for row in range(self.cell_height):
            row += 2
            if row % 2 == 0:
                for column in range(self.cell_width):
                    if column % 2 == 0:
                        checker1_rect = pygame.Rect(column * self.cell_size,
                                                    row * self.cell_size,
                                                    self.cell_size,
                                                    self.cell_size)
                        pygame.draw.rect(self.screen, color_one, checker1_rect)
            else:
                for column in range(self.cell_width):
                    if column % 2 != 0:
                        checker1_rect = pygame.Rect(column * self.cell_size,
                                                    row * self.cell_size,
                                                    self.cell_size,
                                                    self.cell_size)
                        pygame.draw.rect(self.screen, color_one, checker1_rect)


if __name__ == '__main__':
    game = Game((17*30), (17*30), 30, 17, 15)
    game.main()
