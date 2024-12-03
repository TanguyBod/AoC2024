import numpy as np

total_1 = 0
total_2 = 0
__path__ = './J2/input.txt'

with open(__path__, 'r') as file:
    data = file.read().splitlines()

# Part 1
for line in data :
    numbers = line.split()
    direction = np.sign(int(numbers[1]) - int(numbers[0]))
    if direction == 0 or abs(int(numbers[1]) - int(numbers[0])) > 3 :
        continue
    valid = True
    for i in range(1, len(numbers)):
        difference = int(numbers[i]) - int(numbers[i-1])
        if (abs(difference) > 3 or difference == 0) :
            valid = False
            break
        if (np.sign(difference) != direction) :
            valid = False
            break
    if valid :
        total_1 += 1


print("Total part 1: ", total_1)

# Part 2
def isSafe(liste) :
    direction = np.sign(liste[1] - liste[0])
    if direction == 0 or abs(liste[1] - liste[0]) > 3 :
        return 1
    valid = True
    for i in range(1, len(liste)) :
        difference = liste[i] - liste[i-1]
        if (abs(difference) > 3 or difference == 0) :
            valid = False
            return i
        if (np.sign(difference) != direction) :
            valid = False
            return i
    return -1

for line in data :
    numbers = [int(x) for x in line.split()]
    result = isSafe(numbers)
    if result == -1 :
        total_2 += 1
    else :
        for i in range(len(numbers)) :
            number_copy = numbers.copy()
            number_copy.pop(i)
            new_result = isSafe(number_copy)
            if new_result == -1 :
                total_2 += 1
                break

print("Total part 2: ", total_2)