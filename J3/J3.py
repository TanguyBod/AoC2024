import numpy as np

total_1 = 0
total_2 = 0
__path__ = './J3/input.txt'

with open(__path__, 'r') as file:
    data = file.read().splitlines()

def checkMul(characters, i):
    if characters[i] == "m":
        if characters[i+1] == "u":
            if characters[i+2] == "l":
                if characters[i+3] == "(":
                    # Found the start of the function
                    idx = i+4
                    while characters[idx].isdigit():
                        idx += 1
                    if characters[idx] == ",":
                        coma = idx
                        idx += 1
                        while characters[idx].isdigit():
                            idx += 1
                        if characters[idx] == ")":
                            # Found the end of the function
                            nb1 = ""
                            for i in range(i+4, coma):
                                nb1 += characters[i]
                            nb2 = ""
                            for i in range(coma+1, idx):
                                nb2 += characters[i]
                            return (int(nb1) * int(nb2), idx)
    return (0, i)

def checkDo(characters, i):
    # Pattern to find: "do()""
    length = len(characters)
    if (length-i <= 4):
        return False
    str = characters[i] + characters[i+1] + characters[i+2] + characters[i+3]
    if str == "do()":
        return True
    else :
        return False
    
def checkDont(characters, i):
    # Pattern to find: "don't()"
    length = len(characters)
    if (length-i <= 7):
        return False
    str = characters[i] + characters[i+1] + characters[i+2] + characters[i+3] + characters[i+4] + characters[i+5] + characters[i+6]
    if str == "don't()":
        return True
    else :
        return False

# Part 1
for line in data:
    characters = list(line)
    for i in range(len(characters)) :
        mul, idx = checkMul(characters, i)
        total_1 += mul
                            
print("Total part 1: ", total_1)

# Part 2
valid = True
for line in data:
    characters = list(line)
    for i in range(len(characters)) :
        if checkDo(characters, i):
            valid = True
        if checkDont(characters, i):
            valid = False
        if valid :
            mul, idx = checkMul(characters, i)
            total_2 += mul

print("Total part 2: ", total_2)