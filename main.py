"""File: main.py
    Team NO: 5
    Author: Connor Schutze
    Description: Executes all of the code and displays it on screen.
"""

from menu import Menu
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
    first_time = True
    tkinter_menu = Menu(False)
    while running:
        if first_time:
            tkinter_menu.main(0)
            first_time = False
        
        if tkinter_menu.pygame_run == True:
            game = Game(screen_width, screen_height, cell_size, cell_width, cell_height, True)
            game.main()
            tkinter_menu.pygame_run = False
        
        if game.menu_run:
            tkinter_menu.root.deiconify()
            tkinter_menu.main(game.score.high_score)
