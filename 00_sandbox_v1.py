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