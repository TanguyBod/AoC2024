import numpy as np

total_1 = 0
total_2 = 0
__path__ = './J8/input.txt'

with open(__path__, 'r') as file:
    map = [list(ligne.strip()) for ligne in file]
        
different_char = []
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] not in different_char and map[i][j] != '.':
            different_char.append(map[i][j])

locations=[]

# Part 1
for char in different_char:
    idxs = np.argwhere(np.array(map) == char)
    for i in range(len(idxs)):
        for j in range(i+1, len(idxs)):
            dir_x = idxs[j][0] - idxs[i][0]
            dir_y = idxs[j][1] - idxs[i][1]
            if(idxs[j][0] + dir_x < len(map[0]) and idxs[j][1] + dir_y < len(map[1]) and idxs[j][0] + dir_x >= 0 and idxs[j][1] + dir_y >= 0):
                if([idxs[j][0] + dir_x, idxs[j][1] + dir_y] not in locations):
                    locations.append([idxs[j][0] + dir_x, idxs[j][1] + dir_y])
            if(idxs[i][0] - dir_x < len(map[0]) and idxs[i][1] - dir_y < len(map[1]) and idxs[i][0] - dir_x >= 0 and idxs[i][1] - dir_y >= 0):
                if([idxs[i][0] - dir_x, idxs[i][1] - dir_y] not in locations):
                    locations.append([idxs[i][0] - dir_x, idxs[i][1] - dir_y])
                    
total_1 = len(locations)

print("Total part 1: ", total_1)

# Part 2
locations_part2 = []

for char in different_char:
    idxs = np.argwhere(np.array(map) == char)
    for i in range(len(idxs)):
        if ([idxs[i][0], idxs[i][1]] not in locations_part2):
            locations_part2.append([idxs[i][0], idxs[i][1]])
        for j in range(i+1, len(idxs)):
            dir_x = idxs[j][0] - idxs[i][0]
            dir_y = idxs[j][1] - idxs[i][1]
            tmp = 1
            while(idxs[j][0] + tmp*dir_x < len(map[0]) and idxs[j][1] + tmp*dir_y < len(map[1]) and idxs[j][0] + tmp*dir_x >= 0 and idxs[j][1] + tmp*dir_y >= 0):
                if([idxs[j][0] + tmp*dir_x, idxs[j][1] + tmp*dir_y] not in locations_part2):
                    locations_part2.append([idxs[j][0] + tmp*dir_x, idxs[j][1] + tmp*dir_y])
                tmp += 1
            tmp = 1
            while(idxs[i][0] - tmp*dir_x < len(map[0]) and idxs[i][1] - tmp*dir_y < len(map[1]) and idxs[i][0] - tmp*dir_x >= 0 and idxs[i][1] - tmp*dir_y >= 0):
                if([idxs[i][0] - tmp*dir_x, idxs[i][1] - tmp*dir_y] not in locations_part2):
                    locations_part2.append([idxs[i][0] - tmp*dir_x, idxs[i][1] - tmp*dir_y])
                tmp += 1

total_2 = len(locations_part2)

print("Total part 2: ", total_2)