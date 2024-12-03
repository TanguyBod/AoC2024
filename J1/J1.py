import numpy as np

list1 = []
list2 = []
total_1 = 0
total_2 = 0

# Part 1

with open('./J1/input.txt', 'r') as file:
    data = file.read().splitlines()
    for line in data:
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))
list1.sort()
list2.sort()

for i in range(len(list1)):
    total_1 += abs(list1[i]-list2[i])

print(total_1)

# Part 2

list1 = np.array(list1)
list2 = np.array(list2)
idx = 0
while (idx < len(list1)) :
    count1 = len(np.argwhere(list1 == list1[idx]))
    count2 = len(np.argwhere(list2 == list1[idx]))
    total_2 += list1[idx] * count2
    idx += max(count1,1)
    

print(total_2)
