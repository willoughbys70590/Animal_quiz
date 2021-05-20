from tkinter import *
from functools import partial  # To prevent unwanted windows
import random

class GameStats:
    def __init__(self, partner, game_history, game_stats):



        # Set up child window (ie: help box)
        self.stats_box = Toplevel()

        # Set up GUI Frame
        self.stats_box = Frame(self.stats_box)
        self.stats_box.grid()

        # Set up Help heading (row 0)
        self.stats_heading_label = Label(self.stats_box, text="Game Statistics",
                                         font="arial 19 bold")
        self.stats_heading_label.grid(row=0)

        # To Export <instructions> (row 1)
        self.export_instructions = Label(self.stats_box,
                                         text="Here are your Game Statistics."
                                              "Please use the Export button to "
                                              "access the results of each "
                                              "question you did", wrap=250,
                                         font="arial 10 italic",
                                         justify=LEFT, fg="green",
                                         padx=10, pady=10)
        self.export_instructions.grid(row=1)


        # Starting balance (row 2)
        self.details_frame = Frame(self.stats_box)
        self.details_frame.grid(row=2)

        # Starting balance (row 2.0)

        self.start_balance_label = Label(self.details_frame,
                                         text="Starting Balance:", font=heading,
                                         anchor="e")
        self.start_balance_label.grid(row=0, column=0, padx=0)

        self.start_balance_value_label = Label(self.details_frame, font=content,
                                         text="${}".format(game_stats[0]), anchor="e")
        self.start_balance_value_label.grid(row=0, column=1, padx=0)

        # Current balance (row 2.2)
        self.current_balance_label = Label(self.details_frame,
                                           text="Current Balance:", font=heading,
                                           anchor="e")
        self.current_balance_label.grid(row=1, column=0, padx=0)

        self.current_balance_value_label = Label(self.details_frame, font=content,
                                                 text="${}".format(game_stats[1]), anchor="e")
        self.current_balance_value_label.grid(row=1, column=1, padx=0)

        if game_stats[1] > game_stats[0] :
            win_loss ="Amount Won:"
            amount = game_stats[1] - game_stats[0]
            win_loss_fg = "green"
        else:
            win_loss = "Amount Lost:"
            amount = game_stats[0] - game_stats[1]
            win_loss_fg = "#660000"

        # Amount won / lost(row 2.3)
        self.wind_loss_label = Label(self.details_frame,
                                     text=win_loss, font=heading,
                                     anchor="e")
        self.wind_loss_label.grid(row=2, column=0, padx=0)

        self.wind_loss_value_label = Label(self.details_frame, font=content,
                                           text="${}".format(amount),
                                           fg=win_loss_fg, anchor="w")
        self.wind_loss_value_label.grid(row=2, column=0, padx=0)

        # Rounds played (row 2.4)
        self.games_played_label = Label(self.details_frame,
                                       text="Rounds Played:", font=heading,
                                        anchor="e")
        self.games_played_label.grid(row=4, column=0, padx=0)

        self.games_played_value_label = Label(self.details_frame, font=content,
                                              text=len(game_history),
                                              anchor="w")
        self.games_played_value_label.grid(row=4, column=1, padx=0)

        # Dismiss button /row 3)
        # Dismiss button (row2)
        self.dismiss_btn = Button(self.details_frame, text="Dismiss",
                                  width=10, bg="#660000", fg="white",
                                  font="arial 15 bold",
                                  command=partial(self.details_frame, partner))
        self.dismiss_btn.grid(row=2, pady=10)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Animal_Quiz")
    something = Start(root)
    root.mainloop()