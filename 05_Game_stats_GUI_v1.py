from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):
        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.push_me_button = Button(text="Push me", command=self.to_stats)
        self.push_me_button.grid(row=1, pady=10)

    def to_stats(self):
        GameStats(self)


class GameStats:
    def __init__(self, partner):
        # Set up child window (ie: help box)
        self.stats_box = Toplevel()

        # Set up GUI Frame
        self.stats_box = Frame(self.stats_box)
        self.stats_box.grid()

        # Set up Help heading (row 0)
        self.stats_heading_label = Label(self.stats_box, text="Quiz Statistics",
                                         font="arial 19 bold")
        self.stats_heading_label.grid(row=0)

        # To Export <instructions> (row 1)
        self.export_instructions = Label(self.stats_box,
                                         text="Here are your Game Statistics."
                                              "Please use the Export button to "
                                              "access the results of each "
                                              "question you did", wrap=250,
                                         font="arial 10 italic",
                                         justify=LEFT, fg="black",
                                         padx=10, pady=10)
        self.export_instructions.grid(row=1)

        # Starting balance (row 2)
        self.details_frame = Frame(self.stats_box)
        self.details_frame.grid(row=2)

        # Starting balance (row 2.0)

        self.start_balance_label = Label(self.details_frame,
                                         text="Starting Balance:", font="arial 15 bold")
        self.start_balance_label.grid(row=0, column=0, padx=0)

        # Current balance (row 2.2)
        self.current_balance_label = Label(self.details_frame,
                                           text="Current Balance:", font="arial 15 bold",
                                           anchor="e")
        self.current_balance_label.grid(row=1, column=0, padx=0)

        # Dismiss button /row 3

        self.quit_button = Button(self.details_frame, text="Quit", fg="white",
                                  bg="#660000", font="Arial 15 bold",
                                  command=self.to_quit, pady=10, width=10,
                                  justify="left")
        self.quit_button.grid(row=5, pady=10, column=0)

    def to_quit(self):
        root.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Animal_Quiz")
    something = Start(root)
    root.mainloop()
