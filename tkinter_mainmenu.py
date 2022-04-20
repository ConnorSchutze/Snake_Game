from tkinter import *
from tkinter.font import BOLD
from PIL import ImageTk, Image

root = Tk()
root.title("SnakeGame")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

img_menu = ImageTk.PhotoImage(Image.open("images\menusnake.png"))
menu_label = Label(root, image=img_menu)
menu_label.place(x=0, y=0, relwidth=1, relheight=1)

t1 = "Start"
t2 = "Quit"
t3 = "Welcome to Snake Game!"
"""set t4 to read the file scoreboard.txt KEEP ONLY THE HIGHEST SCORE IN THERE"""
t4 = "5670"

def score_update():
    score_file = open("score.txt", "r", "w")
    score_file.read(5)
    int(score_file)
    new_score = score_file + 10
    score_file.write(new_score + "   ")
    score_file.close("score.txt")
    
def start():
    """quit the root window here and begin the pygame window thing."""
    print("what?")
    return


welcome_label = Label(root, text=t3, padx=20, pady=20, bg='#006E02', fg='white', font=25).grid(row=0, column=1)
start_button = Button(root, text=t1, command=start, padx=50, pady=15).grid(row=1, column=1)
filler_label = Label(root, text=t4, padx=0, pady=0, bg="#0097FF").grid(row=2, column=1, padx=210, pady=65)
quit_button = Button(root, text=t2, command=quit, padx=1, pady=1).grid(row=3, column=1)


root.mainloop()