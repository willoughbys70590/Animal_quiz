from tkinter import *
from functools import partial  # To prevent unwanted windows
import random
import csv


class Start:
    def __init__(self, parent):
        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.heading_label = Label(self.start_frame,
                                   text="how many questions\n"
                                        "do you want you can\n"
                                        "only pick between 5&10.",
                                   font="arial 10 bold")
        self.heading_label.grid(row=0)

        self.num_questions = Entry(self.start_frame, text="5")
        self.num_questions.grid(row=1, pady=10)

        self.question_low_box = Button(text="5 question", command=self.to_question,
                                       justify=RIGHT)
        self.question_low_box.grid(row=2, pady=10)

        self.question_high_box = Button(text="10 question", command=self.to_question,
                                        justify=LEFT)
        self.question_high_box.grid(row=3, pady=10)

    def to_question(self):
        # retrieve # of questions balance
        question_number = self.num_questions.get()
        print(question_number)

        Question(self, partial)

        # hide start up window
        root.withdraw()


# the Question function is to show the questions and how they are generated
# make sure its not going in alphabet order .
class Question:
    def __init__(self, prevent, parent):

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
                                           command=self.check_answer,
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
        self.correct_answer_label.grid(row=5)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Animal_Quiz")
    something = Start(root)
    root.mainloop()