from tkinter import *
from functools import partial  # To prevent unwanted windows
import random
import csv


class Start:
    def __init__(self, balance):
        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.starting_funds = IntVar(0)

        self.heading_label = Label(self.start_frame,
                                   text="how many questions\n"
                                        "do you want you can\n"
                                        "only pick between 5&10.",
                                   font="arial 10 bold")
        self.heading_label.grid(row=0)

        self.num_questions = Entry(self.start_frame, text="5")
        self.num_questions.grid(row=1, pady=20)

        self.push_me_button = Button(text="Push me", command=self.to_question)
        self.push_me_button.grid(row=2, pady=10)



        # Entry box, Button & Error Label (row 2)
        self.entry_error_frame = Frame(self.start_frame, width=200)
        self.entry_error_frame.grid(row=2)


        self.amount_error_label = Label(self.entry_error_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.amount_error_label.grid(row=1, columnspan=2, pady=5)

    def to_question(self):
        # retrieve # of questions balance
        question_number = self.num_questions.get()
        print(question_number)

        Question(self)

        # hide start up window
        root.withdraw()


# the Question function is to show the questions and how they are generated
# make sure its not going in alphabet order .
class Question:
    def __init__(self, starting_number):

        # **** initiallise variables ****
        self.balance = IntVar()
        # set starting balance to amount entered by user at start of game
        self.balance.set(starting_number)

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
        # Also need to put a textbox in so they can put there answer in.

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

        # Check answer export frame

        self.Check_answer_export_frame = Frame(self.quiz_box)
        self.Check_answer_export_frame.grid(row=5, pady=10)

        self.Check_answer_button = Button(self.Check_answer_export_frame,
                                           text="Check answer",
                                           font="Arial 10 bold",
                                           command=self.check_answear,
                                           padx=10, pady=10)
        self.Check_answer_button.grid(row=5, pady=5)

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
        answear_num = self.answear_box.get()
        print("Your Answear:", answear_num)

    def check_answer(self):

        correct_ans = " "
        wrong_ans = " "

        if answear == answear_num:
          print("correct")
        elif answear != answear_num:
            print("wrong")

        # printing your answaer that you have put in
        user_ans = self.answer_box.get()
        print("Your answer:", user_ans)

        if answer == user_ans:
            correct_ans = "correct"
            self.answer_box.config(text=user_ans, bg="green")
        elif answer != user_ans:
            wrong_ans = "wrong"
            self.answer_box.config(text=answer, bg="pink")

        # answer label blank for the wrong or correct answear

        self.correct_answer_label = Label(self.quiz_box, text=(correct_ans, wrong_ans), font="Arial 10" )
        self.correct_answer_label.grid(row=3)


    def Number_questions(self):

        starting_number = [0]
        try:
            starting_number = int(starting_number)

            if starting_number < 1:
                has_errors = "yes"
                error_feedback = "Sorry the you need to \n" \
                                 "complete atleast one question."
            elif starting_number > 10:
                has_errors ="yes"
                error_feedback = " Too high! there are only 10/n" \
                                 "questions"

        except ValueError:
            has_errors ="yes"
            error_feedback ="plaase do atleast one question (no numbers / decimals)"

            if has_errors == "yes":
                self.start_amount_entry.config(bg=error_back)
                self.amount_error_label.config(text=error_feedback)

                Start(starting_number)




# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Animal_Quiz")
    something = Start(root)
    root.mainloop()