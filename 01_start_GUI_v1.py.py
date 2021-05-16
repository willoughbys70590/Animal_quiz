from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Start:
    def __init__(self, prevent):
        # Make the starting frame and how wide and height is going to be
        self.start_frame = Frame(padx=90, pady=230)
        self.start_frame.grid()

        # Animal quiz heading, make sure its in the center,text size is readerable and colour
        self.Animal_quiz_label = Label(self.start_frame,
                                       text="Animal quiz",
                                       font="Arial 19 bold")
        self.Animal_quiz_label.grid(row=0)

        


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Animal_Quiz")
    something = Start(root)
    root.mainloop()
