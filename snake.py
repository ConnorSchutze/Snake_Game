"""File: snake.py
   Team NO: 5
   Author: Connor Schutze
   Description: Snake class script, creates the snake object.
"""

import pygame
from pygame.math import Vector2

class Snake:
    """Creating a snake character."""
    def __init__(self, cell_size):
        """"Getting the size of each snake body, settings the snakes
        position and direction.
        """
        pygame.init()
        self.cell_size = cell_size
        self.screen = pygame.display.get_surface()
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_body = False

        # Snake Images
        self.head_up = pygame.image.load("Images/head1.png").convert_alpha()
        self.head_down = pygame.image.load("Images/head3.png").convert_alpha()
        self.head_left = pygame.image.load("Images/head4.png").convert_alpha()
        self.head_right = pygame.image.load("Images/head2.png").convert_alpha()
        
        self.butt_up = pygame.image.load("Images/butt.png").convert_alpha()
        self.butt_down = pygame.image.load("Images/butt3.png").convert_alpha()
        self.butt_left = pygame.image.load("Images/butt4.png").convert_alpha()
        self.butt_right = pygame.image.load("Images/butt2.png").convert_alpha()
        
        self.straight_vertical = pygame.image.load("Images/straight1.png").convert_alpha()
        self.straight_horizontal = pygame.image.load("Images/straight2.png").convert_alpha()
        
        self.turn_one = pygame.image.load("Images/turn4.png").convert_alpha() # Wrong
        self.turn_two = pygame.image.load("Images/turn3.png").convert_alpha() # Wrong
        self.turn_three = pygame.image.load("Images/turn1.png").convert_alpha() # Correct
        self.turn_four = pygame.image.load("Images/turn2.png").convert_alpha() # Wrong

        # Sound
        self.eat_sound = pygame.mixer.Sound("Audio/applause.wav")
    
    def draw(self):
        """Drawing every snake body onto the display surface."""
        self.direction_draw_head()
        self.direction_draw_butt()

        for index, snake_block in enumerate(self.body):
            x_position = int(snake_block.x * self.cell_size)
            y_position = int(snake_block.y * self.cell_size)
            snake_block_rect = pygame.Rect(x_position, y_position, 
                                        self.cell_size, self.cell_size)
            
            if index == 0:
                self.screen.blit(self.head, snake_block_rect)
            elif index == len(self.body) - 1:
                self.screen.blit(self.butt, snake_block_rect)
            else:
                last_body = self.body[index + 1] - snake_block
                next_body = self.body[index - 1] - snake_block

                if last_body.x == next_body.x:
                    self.screen.blit(self.straight_vertical, snake_block_rect)
                elif last_body.y == next_body.y:
                    self.screen.blit(self.straight_horizontal, snake_block_rect)
                else:
                    if last_body.x == -1 and next_body.y == -1 or last_body.y == -1 and next_body.x == -1: # Going right then up / going down then left
                        self.screen.blit(self.turn_one, snake_block_rect)
                    elif last_body.x == -1 and next_body.y == 1 or last_body.y == 1 and next_body.x == -1: # Going right then down / going up then left
                        self.screen.blit(self.turn_two, snake_block_rect)
                    elif last_body.x == 1 and next_body.y == -1 or last_body.y == -1 and next_body.x == 1: # Going left then up / going down then right
                        self.screen.blit(self.turn_three, snake_block_rect)
                    elif last_body.x == 1 and next_body.y == 1 or last_body.y == 1 and next_body.x == 1: # Going left then down / going up then right:
                        self.screen.blit(self.turn_four, snake_block_rect)

    def direction_draw_head(self):
        snake_head_direction = self.body[1] - self.body[0]

        if snake_head_direction == Vector2(1, 0):
            self.head = self.head_left
        elif snake_head_direction == Vector2(-1, 0):
            self.head = self.head_right
        elif snake_head_direction == Vector2(0, 1):
            self.head = self.head_up
        elif snake_head_direction == Vector2(0, -1):
            self.head = self.head_down
    
    def direction_draw_butt(self):
        snake_butt_direction = self.body[1] - self.body[0]

        if snake_butt_direction == Vector2(1, 0):
            self.butt = self.butt_left
        elif snake_butt_direction == Vector2(-1, 0):
            self.butt = self.butt_right
        elif snake_butt_direction == Vector2(0, 1):
            self.butt = self.butt_up
        elif snake_butt_direction == Vector2(0, -1):
            self.butt = self.butt_down

    def movement(self, started):
        """The movement of every snake body to its next position."""
        if started:
            if self.new_body == True:
                og_body = self.body
                og_body.insert(0, og_body[0] + self.direction)
                self.body = og_body
                self.new_body = False
            else:
                og_body = self.body[:-1]
                og_body.insert(0, og_body[0] + self.direction)
                self.body = og_body
    
    def new_snake_body(self):
        """Check to see if the snake needs a new body."""
        self.new_body = True
    
    def play_eat_sound(self):
        self.eat_sound.play()
    
    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
