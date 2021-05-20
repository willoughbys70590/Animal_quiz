import random

test_list = [
    ['cow', 'calf'], 
    ['chicken', 'egg'],
    ['dog', 'puppy']

]

pair = random.choice(test_list)

adult = pair[0]
question = "What is the name of a baby? {}".format(adult)
answer = pair[1]
print()
print(question, answer)
print()
print()


def number_checker(self):
    question_number = self.start_question_number.get()

    # Set error background colours (self assume that there are no
    # Errors at the start...
    error_back = "#ffafaf"
    has_errors = "no"

    # Change backgrounds to white  (for testing purposes) ...
    self.start_question_number.config(bg="white")
    self.start_question_number.config(text="")

    try:
        question_number = int(question_number)

        if question_number < 1:
            has_errors = "yes"
            error_feedback = "Sorry, you need need at least " \
                             "one question"
        elif question_number > 5:
            has_errors = "yes"
            error_feedback = "Too high! the most questions " \
                             "you can do it 5"
    except ValueError:
        has_errors = "yes"
        error_feedback = "Please answear one question(No number / decimal) "

    if has_errors == "yes":
        self.start_question_number.config(bg=error_back)
        self.amount_error_label.config(text=error_feedback)

    else:
        # set starting balance to amount enterrd by users
        self.starting_number.set(question_number)
        self.start_question_number.config(bg="white")
        self.start_question_number.config(text="")


