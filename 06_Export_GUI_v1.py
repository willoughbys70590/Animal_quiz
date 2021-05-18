from tkinter import *
from functools import partial  # To prevent unwanted windows
import random

class Export:
    def __init__(self, partner, game_history, all_game_stats):

        print(game_history)

        # Disable export button
        partner.export_button.config(state=DISABLED)

        # sets up child window (ie: export box)
        self.export_box = Toplevel()

        # 'releaseds' export button
        self.export_box.protocol('WM_DELETE WINDOW',
                                 partial(self.close_export, partner))

        # set up GUI frame
        self.export_frame = Frame(self.export_box, width=300)
        self.export_frame.grid()

        # set up export heading (row 0)
        self.how_heading = Label(self.export_frame,
                                 text="Export / Instructions",
                                 font="arial 14 bold")
        self.how_heading.grid(row=0)

        # export Instructions (lable, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename in the "
                                                         "box bellow and press the"
                                                         "Save button to save your"
                                                         "calculation history to"
                                                         "text file",
                                 justify=LEFT, width=40, wrap=250)
        self.export_text.grid(row=1)

        # Warning text (label, row 2)
        self.export_text = Label(self.export_frame, text="if the filename you "
                                                         "enter below already"
                                                         "exists , its contents"
                                                         "will be replaced with "
                                                         "your calculation history",
                                 justify=LEFT, bg="#ffafaf", fg="maroon",
                                 font="Arial 10 italic", wrap=225, padx=10,
                                 pady=10)
        self.export_text.grid(row=2, pady=10)

        # filename enter box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error Message Lables (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon")
        self.save_error_label.grid(row=4)

        # save / cancel frame(row 4)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # save and cancel Buttons (row 0 of save cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="save",
                                  font="Arial 14 bold", bg="#003366", fg="white",
                                  command=partial(lambda: self.save_history(partner, game_history)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export, partner,))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, game_history, game_stats):

        # Regular expression to cheak filename is valid
        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"

            else:
                problem = ("(no {} 's allowed)".format(letter))
            has_errors = "yes"
            break

        if filename == "":
            problem = "cant be blank"
            has_errors = "yes"

        if has_error == "yes":
            # Display error Message
            self.save_error_label.config(text="Invalid filename - {}".format(problem))
            # Change entry background to pink
            self.filename_entry.config(bg="#ffafaf")
            print()

        else:
            # if there are no errors, generate text file and then close dialogue
            # add .txt suffix!
            filename = filename + ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # heading for text file...
            f.write("Game statistics\n\n")

            # Add new line at the end of each item
            for item in game_stats:
                f.write(round + "\n")

            # Heading for Rounds
            f.write("\nRound Details\n\n")

            # Add new line at end of each of each item
            for item in game_history:
                f.write(item + "\n")

            # close File
            f.close()

            # Close dialogue
            self.close_export(partner)

    def close_export(self, partner):
        # put export button back to normal..
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Animal_Quiz")
    something = Start(root)
    root.mainloop()