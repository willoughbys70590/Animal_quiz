from tkinter import *
from functools import partial  # To prevent unwanted windows
import random

# The start function is to show the title of the quiz little instructions  and a start button
class Start:
    def __init__(self, prevent):
        # Make the starting frame and how wide and height is going to be
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Mystery Heading (row 0)
        self .Animal_quiz_label = Label(self.start_frame, text="Animal Quiz",
                                        font="Arial 19 bold")
        self.Animal_quiz_label.grid(row=1)

        # Help Button
        self.help_button = Button(self.start_frame, text="Help",
                                  command=self.to_help)
        self.help_button.grid(row=2, pady=10)

    def to_help(self):
        get_help = Help(self)

# if they get stuck they can click the help button and it will give them the instructions 
class Help:
    def __init__(self, partner):

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Set up child window (ie: help box)
        self.help_box = Toplevel()

        # if users cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI frame
        self.help_frame = Frame(self.help_box, width=300)
        self.help_frame.grid()

        # Set up help heading (row 0 )
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="arial 14 bold")
        self.how_heading.grid(row=0)

        help_text="To start the quiz first you need to press the satrt button."\
                    "After you have pressed the start button you will then have to"\
                    "answear the question. The Adult annimal name will keep "\
                    "changing so you will need to keep finding out what the baby name"\
                    "is. You will only get 5 turns."
                  

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text=help_text,
                               justify=LEFT, wrap=400, padx=10, pady=10)
        self.help_text.grid(row=1)

        # Dismiss button (row2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, bg="#660000", fg="white",
                                  font="arial 15 bold", 
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)


    def close_help(self, partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Animal_Quiz")
    something = Start(root)
    root.mainloop()