"""File: snake.py
   Team NO: 5
   Author: Connor Schutze
   Description: Snake class script, creates the snake object.
"""

import pygame
from pygame.math import Vector2

class Snake:
   def __init__(self, cell_size):
      pygame.init()
      self.cell_size = cell_size
      self.color = (255, 255, 255)
      self.screen = pygame.display.get_surface()

      self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
      self.direction = Vector2(1, 0)
      self.new_body = False
   
   def draw(self):
      for snake_block in self.body:
         x_position = int(snake_block.x * self.cell_size)
         y_position = int(snake_block.y * self.cell_size)
         snake_block_rect = pygame.Rect(x_position, y_position, 
                                       self.cell_size, self.cell_size)
         pygame.draw.rect(self.screen, self.color, snake_block_rect)

   def movement(self):
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
      self.new_body = True
