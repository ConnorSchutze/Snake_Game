"""File: main.py
   Team NO: 5
   Author: Connor Schutze
   Description: Executes all of the code and displays it on screen.
"""

import pygame
import sys
# import tkinter_mainmenu
from game import Game

# main.py -> 1 -> 2
# 1. main menu - tkinter (menu.py)
   # tkinter function (paramter = highscore)
   # tkinter window run
   # tkinter window close
# 2. snake game - pygame (snake.py, food.py, score.py)

# Directory ->(Adding) # Staging Area ->(Committing) # Git ->(Push) -> Github

cell_size = 40
cell_width = 17
cell_height = 15

screen_width = cell_size * cell_width
screen_height = screen_width

fps = 60

if __name__ == '__main__':
   running = True

   while running:
      pygame_run = True
      # tkinter class

      if pygame_run == True:
         game = Game(screen_width, screen_height, fps)
         game.main()

      
