from tkinter import *
from functools import partial  # To prevent unwanted windows
import random
import csv
class Start:
    def __init__(self, partial):
        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        starting_balance = IntVar(0)

        self.heading_label = Label(self.start_frame,
                                   text="how many questions\n"
                                        "do you want you can\n"
                                        "only pick between 5&10.",
                                   font="arial 10 bold")
        self.heading_label.grid(row=0)

        self.num_questions_entry = Entry(self.start_frame, text="5")
        self.num_questions_entry.grid(row=1, pady=10)

        self.add_question_button = Button(self.start_frame,
                                          font="Arial 14 bold",
                                          text="Add questions",
                                          command=self.check_question_num)
        self.add_question_button.grid(row=2)

        self.amount_error_label = Label(self.start_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.amount_error_label.grid(row=3, columnspan=2, pady=5)

        self.question_low_box = Button(text="5 question", command=self.to_question)
        self.question_low_box.grid(row=4, pady=10)

        self.question_high_box = Button(text="10 question", command=self.to_question)
        self.question_high_box.grid(row=5, pady=10)

        # Disable all the buttons
        self.question_low_box.config(state=DISABLED)
        self.question_high_box.config(state=DISABLED)

    def check_question_num(self):

        has_errors = "no"

        starting_number = self.num_questions_entry.get()

        try:
            starting_number = int(starting_number)

            if starting_number < 5:
                has_errors = "yes"
                error_feedback = "Sorry, the least amount" \
                                 "amount of question you can do is 5"
            elif starting_number > 11:
                has_errors = "yes"
                error_feedback = "Too high! you can only do " \
                                 "10 questions"
            elif starting_number <= 5:
                # enable all the buttons
                self.question_low_box.config(state=NORMAL)
            elif starting_number >= 10:
                self.question_low_box.config(state=NORMAL)
                self.question_high_box.config(state=NORMAL)

        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter amount of question (decimal)"

        if has_errors == "yes":
            self.num_questions_entry.config(bg="red")
            self.amount_error_label.config(text=error_feedback)

            Question(starting_number)

    def to_question(self):

        # retrieve # of questions balance
        question_number = self.num_questions_entry.get()
        print(question_number)

        Question(self)

        # hide start up window
        root.withdraw()

# the Question function is to show the questions and how they are generated
# make sure its not going in alphabet order .
class Question:
    def __init__(self, starting_number):

        print(starting_number)

        self.quiz_box = Toplevel()
        self.quiz_frame = Frame(self.quiz_box)
        self.quiz_frame.grid()

        self.q_adult = StringVar()
        self.a_baby = StringVar()

        # The heading row to play the quiz
        self.heading_label = Label(self.quiz_box, text="Time to start the quiz on how well you know\n"
                                                       " whats the name of the baby animals is.",
                                   font="Arial 10", padx=15, pady=15)
        self.heading_label.grid(row=0)

        # put the question in and make the adult animal keep chaning
        # Also need to put a textbox in so they can put there answear in.

        self.question_label = Label(self.quiz_box, text="Push next to begin your first Question",
                                    font="arial 14 bold")
        self.question_label.grid(row=1)

        # code to import the list and make sure it only says the Adult name not the baby name also

        # text box for the answears (row 4)
        self.text_box_frame = Frame(self.quiz_box, width=200)
        self.text_box_frame.grid(row=2, column=0)

        self.answear_box = Entry(self.text_box_frame,
                                 font="Arial 19 bold", width=10)
        self.answear_box.grid(row=2, column=0)

        with open('animal_list.csv', newline='') as f:
            reader = csv.reader(f)
            animal_list = list(reader)

        # next export frame
        self.next_export_frame = Frame(self.quiz_box)
        self.next_export_frame.grid(row=4, pady=10, column=0)

        self.next_button = Button(self.next_export_frame, text="next",
                                  justify=LEFT,


                                  command=lambda: self.make_question(animal_list),
                                  pady=10, width=10, font="Arial 10 bold")
        self.next_button.grid(row=4, padx=5)

        # Check answear export frame
        self.Check_answear_export_frame = Frame(self.quiz_box)
        self.Check_answear_export_frame.grid(row=5, pady=10)

        self.Check_answear_button = Button(self.Check_answear_export_frame,
                                           text="Check answear",
                                           font="Arial 10 bold",
                                           command=self.check_answer,
                                           padx=10, pady=10)
        self.Check_answear_button.grid(row=5, pady=5)

    def make_question(self, question_list):

        pair = random.choice(question_list)
        adult = pair[0]
        answear = pair[1]

        # put question and answear in string variable so we can use it in checking function
        self.a_baby.set(answear)

        self.question_label.config(text="What is the name for a young?"
                                        "\n {}".format(adult))
        # print(adult)
        # print("answear", answear)

    def check_answer(self):

        correct_ans = ""
        wrong_ans = ""

        # The real answear from my csv list
        answear = self.a_baby.get()
        print("Check answear:", answear)

        # printing your answaer that you have put in
        user_ans = self.answear_box.get()
        print("Your Answear:", user_ans)

        if answear == user_ans:
            correct_ans = "correct"
            self.answear_box.config(bg="green")
        elif answear != user_ans:
            wrong_ans = "wrong"
            self.answear_box.config(bg="pink")

        self.correct_answer_label = Label(self.quiz_box, text=(correct_ans, wrong_ans),
                                          font="Arial")
        self.correct_answer_label.grid(row=3)

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
        # Dismiss button /row 3)
        # Dismiss button (row2)
        self.dismiss_btn = Button(self.details_frame, text="Dismiss",
                                  width=10, bg="#660000", fg="white",
                                  font="arial 15 bold",
                                  command=partial(self.details_frame, partner))
        self.dismiss_btn.grid(row=2, pady=10)


class Export:
    def __init__(self, partner):

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