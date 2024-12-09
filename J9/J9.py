import numpy as np

total_1 = 0
total_2 = 0
__path__ = './J9/input.txt'

with open(__path__, 'r') as file:
    data = file.read().splitlines()
str_array = list(data[0].strip())
int_array = [int(x) for x in str_array]

block_array = []
id = 0
for i in range (len(int_array)):
    for nb in range(int_array[i]):
        if i%2 == 0:
            block_array.append(id)
        else :
            block_array.append(".")
    if i%2 == 0:
        id += 1
block_array_2 = block_array.copy()

# Part 1
def get_first_empty(block_array):
    for i in range(len(block_array)):
        if block_array[i] == ".":
            return i
    return -1

def get_last_full(block_array):
    for i in range(len(block_array)-1, -1, -1):
        if block_array[i] != ".":
            return i
    return -1

def order_array(block_array) :
    first_empty = get_first_empty(block_array)
    last_full = get_last_full(block_array)
    while first_empty < last_full:
        block_array[first_empty], block_array[last_full] = block_array[last_full], block_array[first_empty]
        first_empty = get_first_empty(block_array)
        last_full = get_last_full(block_array)
    return block_array

ordered_array = order_array(block_array)
first_empty = get_first_empty(ordered_array)
order_array = ordered_array[:first_empty]
for i in range(len(order_array)):
    total_1 += order_array[i]*i

print("Total part 1: ", total_1)

# Part 2

def get_length_of_block(block_array, id):
    count = 0
    for i in range(len(block_array)):
        if block_array[i] == id:
            count += 1
    return count

def get_fist_occurence(block_array, id):
    for i in range(len(block_array)):
        if block_array[i] == id:
            return i
    return -1

def get_first_empty_block(block_array, size) :
    count = 0
    for i in range (len(block_array)):
        if block_array[i] == ".":
            count += 1
        else :
            count = 0
        if count == size:
            return i - size + 1
    return -1

def order_array_2(block_array) :
    maximum = id -1
    for i in range(maximum, -1, -1) :
        length = get_length_of_block(block_array, i)
        first_occurence = get_fist_occurence(block_array, i)
        first_empty = get_first_empty_block(block_array, length)
        if first_empty != -1 and first_empty < first_occurence:
            for j in range(length):
                block_array[first_empty+j] = i
                block_array[first_occurence+j] = "."
    return block_array

ordered_array_2 = order_array_2(block_array_2)

for i in range(len(ordered_array_2)):
    if ordered_array_2[i] != ".":
        total_2 += ordered_array_2[i]*i

print("Total part 2: ", total_2)