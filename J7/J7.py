import numpy as np

total_1 = 0
total_2 = 0
__path__ = './J7/input.txt'

with open(__path__, 'r') as file:
    data = file.read().splitlines()

equations = []
for line in data:    
    total = int(line.split(":")[0])
    equation = [int(x) for x in line.split(":")[1].split()]
    equation.reverse()
    equations.append((total, equation))

# Part 1
def allPossibilities(equation):
    possibilities = []
    if(len(equation) == 1):
        return [equation[0]]
    else :
        possibilitiesRecursion = allPossibilities(equation[1:])
        for possibility in possibilitiesRecursion:
            possibilities.append(equation[0] + possibility)
            possibilities.append(equation[0] * possibility)
    return possibilities

for total, equation in equations:
    possibilities = allPossibilities(equation)
    if total in possibilities:
        total_1 += total
print("Total part 1: ", total_1)

# Part 2

def allPossibilities2(equation):
    possibilities = []
    if (len(equation) == 2):
        return [equation[0]+equation[1], equation[0]*equation[1], int(str(equation[1])+str(equation[0]))]
    else :
        possibilitiesRecursion = allPossibilities2(equation[1:])
        for possibility in possibilitiesRecursion:
            possibilities.append(equation[0] + possibility)
            possibilities.append(equation[0] * possibility)
            possibilities.append(int(str(possibility) + str(equation[0])))
    return possibilities

for total, equation in equations:
    possibilities = allPossibilities2(equation)
    if total in possibilities:
        total_2 += total

print("Total part 2: ", total_2)