from tkinter import *
from tkinter.font import BOLD
from PIL import ImageTk, Image
import sys



class Menu():
    def __init__(self, pygame_run):
        self.pygame_run = pygame_run

    def main(self, high_score):
        self.high_score = str(high_score)

        self.root = Tk()
        self.root.title("SnakeGame")
        self.root.minsize(width=400, height=400)
        self.root.maxsize(width=400, height=400)
        self.t1 = "Start"
        self.t2 = "Quit"
        self.t3 = "Welcome to Snake Game!"
        """set t4 to read the file scoreboard.txt KEEP ONLY THE HIGHEST SCORE IN THERE"""
        self.t4 = self.high_score
        self.img_menu = ImageTk.PhotoImage(Image.open("Images\menusnake.png"))
        self.menu_label = Label(self.root, image=self.img_menu).place(x=0, y=0, relwidth=1, relheight=1)
        self.welcome_label = Label(self.root, text=self.t3, padx=20, pady=20, bg='#006E02', fg='white', font=25).grid(row=0, column=1)
        self.start_button = Button(self.root, text=self.t1, command=self.start, padx=50, pady=15).grid(row=1, column=1)
        self.filler_label = Label(self.root, text=self.t4, padx=0, pady=0, bg="#0097FF").grid(row=2, column=1, padx=210, pady=65)
        self.quit_button = Button(self.root, text=self.t2, command=quit, padx=1, pady=1).grid(row=3, column=1)
        self.welcome_label = Label(self.root, text=self.t3, padx=20, pady=20, bg='#006E02', fg='white', font=25).grid(row=0, column=1)
        self.start_button = Button(self.root, text=self.t1, command=self.start, padx=50, pady=15).grid(row=1, column=1)
        self.filler_label = Label(self.root, text=self.t4, padx=0, pady=0, bg="#0097FF").grid(row=2, column=1, padx=210, pady=65)
        self.quit_button = Button(self.root, text=self.t2, command=quit, padx=1, pady=1).grid(row=3, column=1)
        self.root.mainloop()

    def start(self):
        self.pygame_run = True
        self.root.destroy()