import numpy as np

total_1 = 0
total_2 = 0
__path__ = './J10/input.txt'

with open(__path__, 'r') as file:
    data = file.read().splitlines()
    map = [list(ligne.strip()) for ligne in data]
        
# Part 1
nineAccessibles = []

def number_adjacent(map, i, j, number) :
    list_co = []
    if i > 0 and map[i-1][j] == number :
        list_co.append((i-1, j))
    if i < len(map) - 1 and map[i+1][j] == number :
        list_co.append((i+1, j))
    if j > 0 and map[i][j-1] == number :
        list_co.append((i, j-1))
    if j < len(map[0]) - 1 and map[i][j+1] == number :
        list_co.append((i, j+1))
    return list_co

def leadToNine(map, i, j) :
    nineReacheable = []
    nb = int(map[i][j])
    if nb == 9 :
        nineReacheable.append([i, j])
        return nineReacheable
    else :
        list_co = number_adjacent(map, i, j, str(nb+1))
        for co in list_co :
            result = leadToNine(map, co[0], co[1])
            for res in result :
                nineReacheable.append(res)
        return nineReacheable

list_0 = np.argwhere(np.array(map) == '0')

for co in list_0 :
    a = leadToNine(map, co[0], co[1])
    a = list(set([tuple(x) for x in a]))
    total_1 += len(a)

print("Total part 1: ", total_1)

# Part 2

list_0 = np.argwhere(np.array(map) == '0')

for co in list_0 :
    a = leadToNine(map, co[0], co[1])
    total_2 += len(a)

print("Total part 2: ", total_2)