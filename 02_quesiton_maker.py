# code to import the list and make sure it only says the Adult name not the baby name also
import random

import csv

with open('Animal_list.csv', newline='') as f:
    reader = csv.reader(f)
    Animal_list = list(reader)

Animal= random.choice(Animal_list)
adult = Animal[0]
question = "what is the name of a baby? {}".format(adult)
print(question)




