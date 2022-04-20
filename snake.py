"""File: snake.py
   Team NO: 5
   Author: Connor Schutze
   Description: Snake class script, creates the snake object.
"""

import pygame
from pygame.math import Vector2

class Snake:
   def __init__(self):
      pygame.init()
      self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
   
   def draw(self):
      pass