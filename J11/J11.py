import numpy as np

total_1 = 0
total_2 = 0
__path__ = './J11/input.txt'

with open(__path__, 'r') as file:
    data = file.read().splitlines()

input = [int(x) for x in data[0].split(" ")]
input2 = input.copy()

# Part 1

def nextBlink(array) :
    skip = False
    buffer = 0
    for i in range (0, len(array)):
        if array[i+buffer] == 0:
            array[i+buffer] = 1
            continue
        elif len(str(array[i+buffer]))%2 == 0:
            firstHalf = str(array[i+buffer])[:len(str(array[i+buffer]))//2]
            secondHalf = str(array[i+buffer])[len(str(array[i+buffer]))//2:]
            array[i+buffer] = int(firstHalf)
            array.insert(i+buffer+1, int(secondHalf))
            buffer += 1
            continue
        else:
            array[i+buffer] = 2024*array[i+buffer]
    return array

for i in range(25) :
    input = nextBlink(input)

total_1 = len(input)
print("Total part 1: ", total_1)

# Part 2

def score(number, remaining, memo={}):
    if (number, remaining) in memo:
        return memo[(number, remaining)]
    if remaining == 0:
        return 1
    if number == 0:
        result = score(1, remaining - 1, memo)
    elif len(str(number))%2 == 0 :
        result = score(int(str(number)[:len(str(number))//2]), remaining - 1, memo) + score(int(str(number)[len(str(number))//2:]), remaining - 1, memo)
    else:
        result = score(2024 * number, remaining - 1, memo)
    memo[(number, remaining)] = result
    return result

def blinks(array, nbBlinks) :
    total = 0
    for i in range(len(array)) :
        total += score(array[i], nbBlinks)
    return total

total_2 = blinks(input2, 75)

print("Total part 2: ", total_2)