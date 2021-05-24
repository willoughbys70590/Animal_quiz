from tkinter import *
from functools import partial  # To prevent unwanted windows
import random

from tkinter import *
from functools import partial  # To prevent unwanted windows
import random
import csv


# The start function is to show the title of the quiz little instructions  and a start button
class Start:
    def __init__(self):
        # Make the starting frame and how wide and height is going to be
        self.start_frame = Frame(padx=15, pady=15)
        self.start_frame.grid()

        # Animal quiz heading, make sure its in the center,text size is readerable and colour
        # Heading in row 0
        self.Animal_quiz_label = Label(self.start_frame,
                                       text="Animal Quiz",
                                       font="Arial 20 bold")
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
        self.start_quiz_button = Button(self.start_frame, text="start", bg="#4da6ff",
                                        command=self.to_question,
                                        font=button_font)
        self.start_quiz_button.grid(row=4, pady=10)

        # Help Button
        self.help_export_frame = Frame(self.start_frame)
        self.help_export_frame.grid(row=5, pady=10)

        self.help_button = Button(self.help_export_frame, text="Help", bg="#ffc34d",
                                  font="Arial 15 bold"
                                  , command=self.to_help,
                                  pady=10, width=10)
        self.help_button.grid(row=5, column=1)

        # Quit button
        self.quit_button = Button(self.help_export_frame, text="Quit", fg="white",
                                  bg="#660000", font="Arial 15 bold",
                                  command=self.to_question, pady=10, width=10,
                                  justify="left")
        self.quit_button.grid(row=5, pady=10, column=0)

        self.num_questions = Entry(self.start_frame, text="5")
        self.num_questions.grid(row=1, pady=10)

    def to_question(self, start_quiz_button):
        # retrieve # of questions balance
        question_number = self.num_questions.get()
        print(question_number)

        Question(self)

    def to_quit(self):
        root.destroy()

    def to_help(self):
        get_help = Help(self)


# the Question function is to show the questions and how they are generated
# make sure its not going in alphabet order .
class Question:
    def __init__(self, prevent, parent):

        self.quiz_box = Toplevel()
        self.quiz_frame = Frame(self.quiz_box)
        self.quiz_frame.grid()

        self.q_baby = StringVar()
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
        self.question_label.grid(row=2)

        # code to import the list and make sure it only says the Adult name not the baby name also

        # text box for the answears (row 4)
        self.text_box_frame = Frame(self.quiz_box, width=200)
        self.text_box_frame.grid(row=4, column=0)

        self.answear_box = Entry(self.text_box_frame,
                                 font="Arial 19 bold", width=10)
        self.answear_box.grid(row=4, column=0)

        with open('animal_list.csv', newline='') as f:
            reader = csv.reader(f)
            animal_list = list(reader)

        # next export frame
        self.next_export_frame = Frame(self.quiz_box)
        self.next_export_frame.grid(row=5, pady=10, column=0)

        self.next_button = Button(self.next_export_frame, text="next",
                                  justify=LEFT,
                                  command=lambda: self.make_question(animal_list),
                                  pady=10, width=10, font="Arial 10 bold")
        self.next_button.grid(row=5, padx=5)

        # Check answear export frame
        self.Check_answear_export_frame = Frame(self.quiz_box)
        self.Check_answear_export_frame.grid(row=6, pady=10)

        self.Check_answear_button = Button(self.Check_answear_export_frame,
                                           text="Check answear",
                                           font="Arial 10 bold",
                                           command=self.check_answear,
                                           padx=10, pady=10)
        self.Check_answear_button.grid(row=6, pady=5)

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

    def check_answear(self):

        # The real answear from my csv list
        answear = self.a_baby.get()
        print("Check answear:", answear)

        # printing your answaer that you have put in
        user_ans = self.answear_box.get()
        print("Your Answear:", user_ans)

        if answear == user_ans:
            print("correct")
        elif answear != user_ans:
            print("wrong")


# This is the Help / Instructions button where they can find out what
# To if they get stuck.
class Help:
    def __init__(self, partner):
        # disable help button
        partner.help_button.config(state=DISABLED)

        # Set up child window (ie: help box)
        self.help_box = Toplevel()

        # if users cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI frame
        self.start_frame = Frame(self.help_box, width=100)
        self.start_frame.grid()

        # Set up help heading (row 0 )
        self.how_heading = Label(self.start_frame, text="Help / Instructions",
                                 font="arial 14 bold")
        self.how_heading.grid(row=0)

        help_text = "To start the quiz first you need to press the satrt button." \
                    "After you have pressed the start button you will then have to" \
                    "answear the question. The Adult annimal name will keep " \
                    "changing so you will need to keep finding out what the baby name" \
                    "is. You will only get 5 turns."

        # Help text (label, row 1)
        self.help_text = Label(self.start_frame, text=help_text,
                               justify=LEFT, wrap=400, padx=10, pady=10)
        self.help_text.grid(row=1)

        # Dismiss button (row2)
        self.dismiss_btn = Button(self.start_frame, text="Dismiss",
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