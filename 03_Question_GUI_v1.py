from tkinter import *
from functools import partial  # To prevent unwanted windows
import random

# code to import the list and make sure it only says the Adult name not the baby name also
import csv

# The start function is to show the title of the quiz little instructions  and a start button
class Start:
    def __init__(self, prevent):
        # Make the starting frame and how wide and height is going to be
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Animal quiz heading, make sure its in the center,text size is readerable and colour
        # Heading in row 0
        self.Animal_quiz_label = Label(self.start_frame,
                                       text="Animal quiz",
                                       font="Arial 25 bold")
        self.Animal_quiz_label.grid(row=0)

        # The first set of instructions that you will need to follow
        # Sub-title in row 1
        self.Animal_instrustions = Label(self.start_frame, font="Arial 10 italic",
                                        text="To start the quiz press "
                                        " the start button to start.",
                                        wrap=275, justify=LEFT, padx=10, pady=10)
        self.Animal_instrustions.grid(row=1)

        # Button font goes here
        button_font = "Arial 15 bold"

        # The start button to start the questions
        self.start_quiz_button = Button(self.start_frame, text="start",
                                command=self.to_quiz,
                            font=button_font, bg="#0000FF")
        self.start_quiz_button.grid(row=4,column=0,pady=10)

        self.start_quiz_button.config(state=NORMAL)

    def to_quiz(self):
        get_quiz = Question(self)


# the Question function is to show the questions and how they are generated 
# make sure its not going in alphabet order.

class Question:
    def __init__(self, prevent):

        # making the question frame of the Starting of the quiz 
        self.Question_frame = Frame(padx=10, pady=10)
        self.Question_frame.grid()



        # input the question maker and and the fit it into the frame
        # code to import the list and make sure it only says the Adult name not the baby name also

        self.Animal_quiz_label = Label(self.Question_frame,
                                text="Animal Quiz",
                                font="Arial 25 bold")
        self.Animal_quiz_label.grid(row=1)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Animal_Quiz")
    something = Start(root)
    root.mainloop()
