"""File: main.py
    Team NO: 5
    Author: Connor Schutze
    Description: Executes all of the code and displays it on screen.
"""

# from menu import Menu
from game import Game

# main.py -> 1 -> 2
# 1. main menu - tkinter (menu.py)
    # tkinter function (paramter = highscore)
    # tkinter window run
    # tkinter window close
# 2. snake game - pygame (snake.py, food.py, score.py)

# Directory ->(Adding) # Staging Area ->(Committing) # Git ->(Push) -> Github

# Snake grid system
cell_size = 30
cell_width = 17
cell_height = 15

# Screen resolution
screen_width = cell_size * cell_width
screen_height = screen_width

if __name__ == '__main__':
    running = True

    while running:
        pygame_run = True
        # tkinter class
        # tkinter class returns pygame_run as False if clicked QUIT button

    if pygame_run == True:
        game = Game(screen_width, screen_height, cell_size, cell_width, cell_height)
        game.main()
