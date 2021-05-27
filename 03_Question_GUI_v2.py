from tkinter import *
from functools import partial  # To prevent unwanted windows
import random
import csv

class Start:
    def __init__(self, partial):
        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

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

        self.question_low_box = Button(text="5 question", command= lambda: self.to_question(5))
        self.question_low_box.grid(row=4, pady=10)

        self.question_high_box = Button(text="10 question", command= lambda: self.to_question(10))
        self.question_high_box.grid(row=5, pady=10)

        # Disable all the buttons
        '''
        self.question_low_box.config(state=DISABLED)
        self.question_high_box.config(state=DISABLED)
        '''

    def check_question_num(self):

        has_errors = "no"

        starting_number = self.num_questions_entry.get()

        try:
            starting_number = int(starting_number)

            if starting_number < 5:
                has_errors = "yes"
                error_feedback = "Sorry, the least amount\n" \
                                 "of question you can do\n" \
                                 "is 5"
            elif starting_number > 10:
                has_errors = "yes"

                error_feedback = "Too high! you can only do\n" \
                                 " highest of 10 questions"
            elif starting_number >= 5:
                # enable all the buttons
                self.question_low_box.config(state=NORMAL)
            elif starting_number >= 10:
                # enable all the buttons
                self.question_low_box.config(state=NORMAL)
                self.question_high_box.config(state=NORMAL)

        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter amount of \n" \
                             "question( no decimal)"

        if has_errors == "yes":
            self.num_questions_entry.config(bg="red")
            self.amount_error_label.config(text=error_feedback)
        else:
            self.num_questions_entry.config(bg="white")
            self.amount_error_label.config(text="")


    def to_question(self, num_questions):

        # retrieve # of questions balance
        # question_number = self.num_questions_entry.get()
        # print(question_number)

        Question(num_questions)

        # hide start up window
        root.withdraw()


# the Question function is to show the questions and how they are generated
# make sure its not going in alphabet order .
class Question:
    def __init__(self, num_questions):

        print(num_questions)

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

        with open('animal_list.csv', newline='') as f:
            reader = csv.reader(f)
            animal_list = list(reader)

        self.correct_answer_label = Label(self.quiz_box, text="",
                                          font="Arial")
        self.correct_answer_label.grid(row=3)

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
                                           command=self.check_answer,
                                           padx=10, pady=10)
        self.Check_answer_button.grid(row=5, pady=5)

    def make_question(self, question_list):

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

        correct_ans = ""
        wrong_ans = ""

        # The real answer from my csv list
        answer = self.a_baby.get()
        print("Check answer:", answer)

        # printing your answaer that you have put in
        user_ans = self.answer_box.get()
        print("Your answer:", user_ans)

        if answer == user_ans:
            feedback = "correct"
            self.answer_box.config(bg="green")
        elif answer != user_ans:
            feedback = "wrong"
            self.answer_box.config(bg="pink")

        self.correct_answer_label.config(text=feedback)

    '''
        self.correct_answer_label = Label(self.quiz_box, text=(correct_ans, wrong_ans),
                                          font="Arial")
        self.correct_answer_label.grid(row=3)
        '''


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Animal_Quiz")
    something = Start(root)
    root.mainloop()