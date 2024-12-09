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

print("Total part 2: ", total_2)