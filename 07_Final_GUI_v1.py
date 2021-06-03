from tkinter import *
from functools import partial  # To prevent unwanted windows
import random
import csv


# The start function is to show the title of the quiz little instructions  and a start button
class Start:
    def __init__(self, partial):
        # Make the starting frame and how wide and height is going to be
        self.start_frame = Frame(padx=15, pady=15)
        self.start_frame.grid()

        # Animal quiz heading, make sure its in the center,text size is readable and colour
        # Heading in row 0
        self.Animal_quiz_label = Label(self.start_frame,
                                       text="Animal Quiz",
                                       font="Arial 20 bold")
        self.Animal_quiz_label.grid(row=0)

        self.heading_label = Label(self.start_frame,
                                   text="how many questions\n"
                                        "do you want you can\n"
                                        "only pick 5 or 10.",
                                   font="arial 10 bold")
        self.heading_label.grid(row=1)

        self.question_low_box = Button(self.start_frame, text="5 question",
                                       command=lambda: self.to_question(5))
        self.question_low_box.grid(row=2, pady=10)

        self.question_high_box = Button(self.start_frame, text="10 question",
                                        command=lambda: self.to_question(10))
        self.question_high_box.grid(row=3, pady=10)

        # Help Button
        self.help_export_frame = Frame(self.start_frame)
        self.help_export_frame.grid(row=4, pady=10)

        self.help_button = Button(self.help_export_frame, text="Help", bg="#ffc34d",
                                  font="Arial 15 bold"
                                  , command=self.to_help,
                                  pady=10, width=10)
        self.help_button.grid(row=0, column=1)

        # Quit button
        self.quit_button = Button(self.help_export_frame, text="Quit", fg="white",
                                  bg="#660000", font="Arial 15 bold",
                                  command=self.to_quit, pady=10, width=10,
                                  justify="left")
        self.quit_button.grid(row=0, pady=10, column=0)


    def to_question(self, num_questions):
        # retrieve # of questions balance
        # question_number = self.num_questions_entry.get()
        # print(question_number)

        Question(self, num_questions)

        # hide start up window
        root.withdraw()

    def to_quit(self):
        root.withdraw()

    def to_help(self):
        get_help = Help(self)

# the Question function is to show the questions and how they are generated
# make sure its not going in alphabet order .
class Question:
    def __init__(self, partner, num_questions):

        print(num_questions)

        # Varibles to hold number of questions needed
        # number of questions asked and correct
        self.questions = IntVar()
        self.num_asked = IntVar()
        self.num_correct = IntVar()
        # set starting amount to the amount that the
        # user put in
        self.questions.set(num_questions)

        # intitlise # ask and # correct to zero
        self.num_asked.set(0)
        self.num_correct.set(0)

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

        # put the question in and make the adult animal keep changing
        # Also need to put a textbox in so they can put there answer in.
        # Disable answer button till they press next

        self.question_label = Label(self.quiz_box, text="Push next to begin your first Question",
                                    font="arial 14 bold")
        self.question_label.grid(row=1)

        # code to import the list and make sure it only says the Adult name not the baby name also

        # text box for the answers (row 4)
        self.text_box_frame = Frame(self.quiz_box, width=200)
        self.text_box_frame.grid(row=2, column=0)

        self.answer_box = Entry(self.text_box_frame,
                                 font="Arial 19 bold", width=10)
        self.answer_box.grid(row=2, column=0)

        # importing the list function
        with open('animal_list.csv', newline='') as f:
            reader = csv.reader(f)
            animal_list = list(reader)

        self.correct_answer_label = Label(self.quiz_box,
                                          text="",font="Arial")
        self.correct_answer_label.grid(row=3)

        self.score_label = Label(self.quiz_box, font="Arial 10 bold",
        text="score goes here", wrap=200)
        self.score_label.grid(row=4, column=0)

        # Check answer export frame
        # disable button
        self.Check_answer_export_frame = Frame(self.quiz_box)
        self.Check_answer_export_frame.grid(row=6, pady=10)

        self.Check_answer_button = Button(self.Check_answer_export_frame,
                                           text="Check answer",
                                           font="Arial 10 bold",
                                           command=self.check_answer,
                                           padx=10, pady=10)
        self.Check_answer_button.grid(row=6, pady=5)
        self.Check_answer_button.config(state=DISABLED)

        # next export frame
        self.next_export_frame = Frame(self.quiz_box)
        self.next_export_frame.grid(row=5, pady=10, column=0)
        self.next_button = Button(self.next_export_frame, text="next",
                                  justify=LEFT,
                                  command=lambda: self.make_question(animal_list),
                                  pady=10, width=10, font="Arial 10 bold")
        self.next_button.grid(row=5, padx=5)




    def make_question(self, question_list):

        # Disabled the next button and then make the check answer enabled

        self.next_button.config(state=DISABLED)
        self.Check_answer_button.config(state=NORMAL)

        # making the text box made white
        self.answer_box.config(bg="white")


        pair = random.choice(question_list)
        adult = pair[0]
        answer = pair[1]

        # put question and answer in string variable so we can use it in checking function
        self.a_baby.set(answer)

        self.question_label.config(text="What is the name for a young?"
                                        "\n {}".format(adult))
        # print(adult)
        # print("answer", answer)


    def check_answer(self):

        # check answer is disabled and then the next button is
        # enabled (only if the quiz is not yet over)
        self.Check_answer_button.config(state=DISABLED)
        self.next_button.config(state=NORMAL)

        asked = self.num_asked.get()
        asked += 1
        self.num_asked.set(asked)
        user_questions = self.questions.get()
        num_correct = self.num_correct.get()

        if asked >= user_questions:
            self.next_button.config(state=DISABLED)
            self.quiz_box.focus()
            self.next_button.config(text="Quiz over")

        # making the text box go back to white
        self.answer_box.config(text=" ")

        # The real answer from my csv list

        answer = self.a_baby.get()
        print("Check answer:", answer)

        # printing your answer that you have put in
        user_ans = self.answer_box.get()
        print("Your answer:", user_ans)
        # print out if answer is correct or id answer is wrong

        if answer == user_ans:
            feedback = "correct"
            self.answer_box.config(bg="green")
            num_correct += 1
            self.num_correct.set(num_correct)
        elif answer != user_ans:
            feedback = "wrong"
            self.answer_box.config(bg="pink")
        self.correct_answer_label.config(text=feedback)

        # the score label to make sure that
        self.score_label.config(text="{} / {}".format( 1 * num_correct, user_questions))


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

        help_text = "To start the quiz you will need\n" \
                    " to first pick how many questions \n" \
                    "you would  like 5 or 10. Then once\n " \
                    "you have done that it will take you\n" \
                    " start answering the questions."

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