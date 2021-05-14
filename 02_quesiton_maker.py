import random 

import csv

with open('Animal_list.csv', newline='') as f:
    reader = csv.reader(f)
    Animal_list = list(reader)

pair = random.choice(Animal_list)

question = "what is the name of a baby? {}".format(pair)
print(question)



