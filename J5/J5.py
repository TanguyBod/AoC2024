import numpy as np

total_1 = 0
total_2 = 0
__path__ = './J5/input.txt'

consignes = []
updates = []
consigne = True

with open(__path__, 'r') as file:
    data = file.read().splitlines()
    for line in data:
        if line == "":
            consigne = False
            continue
        if consigne:
            consignes.append(line.split("|"))
        else:
            updates.append(line.split(","))

print(len(consignes), len(updates))
            
# Part 1
def isUpdateCorrect(update, consignes):
    correct = True
    for consigne in consignes :
        if consigne[0] in update and consigne[1] in update:
            index_0 = update.index(consigne[0])
            index_1 = update.index(consigne[1])
            if index_0 > index_1:
                correct = False
                break
    return correct

for update in updates:
    if isUpdateCorrect(update, consignes):
        milieu = len(update) // 2
        total_1 += int(update[milieu])

print("Total part 1: ", total_1)

# Part 2

incorrect = []
for update in updates:
    if not isUpdateCorrect(update, consignes):
        incorrect.append(update)

def correctUpdate(update, consignes) :
    for consigne in consignes:
        if consigne[0] in update and consigne[1] in update:
            index_0 = update.index(consigne[0])
            index_1 = update.index(consigne[1])
            if index_0 > index_1:
                temp = update[index_0]
                update[index_0] = update[index_1]
                update[index_1] = temp
                return correctUpdate(update, consignes)
    return update

# Need to correct incorrect updates
for update in incorrect:
    corrected_update = correctUpdate(update, consignes)
    milieu = len(corrected_update) // 2
    total_2 += int(corrected_update[milieu])

print("Total part 2: ", total_2)