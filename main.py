"""File: main.py.

Team NO: 5
Author: Connor Schutze and Zac Ohran
Description: Executes all of the code and displays it on screen.
"""

from menu import Menu
from game import Game

# Snake grid system
cell_size = 30
cell_width = 17
cell_height = 15

# Screen resolution
screen_width = cell_size * cell_width
screen_height = screen_width

if __name__ == '__main__':
    running = True
    tkinter_menu = Menu(False)
    game = Game(screen_width, screen_height, cell_size, cell_width,
                cell_height)
    tkinter_menu.main(0)

    if tkinter_menu.pygame_run:
        game.main()
