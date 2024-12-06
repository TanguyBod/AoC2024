import numpy as np

total_1 = 0
total_2 = 0
__path__ = './J6/input.txt'

with open(__path__, 'r') as file:
    map = [list(ligne.strip()) for ligne in file]
position = (0, 0)
visited_cases = []
visited_cases.append(position)
for i in range (len(map[0])) :
    for j in range (len(map[1])) :
        if map[i][j] == '^' :
            position = (i, j)
            break
direction = [-1,0] 
initialPosition = position
initialDirection = direction

# Part 1
def changeDirection(direction) :
    if direction == [-1,0] :
        return [0,1]
    if direction == [0,1] :
        return [1,0]
    if direction == [1,0] :
        return [0,-1]
    if direction == [0,-1] :
        return [-1,0]

def moveToObstacle(position, visited_cases, map, direction) :
    inFrontOf = map[position[0] + direction[0]][position[1] + direction[1]]
    while (inFrontOf != '#') :
        position = (position[0] + direction[0], position[1] + direction[1])
        if position not in visited_cases :
            visited_cases.append(position)
        if (position[0] + direction[0] == -1 or position[0] + direction[0] == len(map[0]) or position[1] + direction[1] == -1 or position[1] + direction[1] == len(map[1])) :
            break
        inFrontOf = map[position[0] + direction[0]][position[1] + direction[1]]
    return position, visited_cases

exit = False
while not exit :
    position, visited_cases = moveToObstacle(position, visited_cases, map, direction)
    if (position[0] + direction[0] == -1 or position[0] + direction[0] == len(map[0]) or position[1] + direction[1] == -1 or position[1] + direction[1] == len(map[1])) :
        exit = True
        break
    direction = changeDirection(direction)

total_1 = len(visited_cases)

print("Total part 1: ", total_1)

# Part 2
def moveToObstacle(position, map, direction) :
    inFrontOf = map[position[0] + direction[0]][position[1] + direction[1]]
    while (inFrontOf != '#') :
        position = (position[0] + direction[0], position[1] + direction[1])
        if (position[0] + direction[0] == -1 or position[0] + direction[0] == len(map[0]) or position[1] + direction[1] == -1 or position[1] + direction[1] == len(map[1])) :
            break
        inFrontOf = map[position[0] + direction[0]][position[1] + direction[1]]
    return position, direction

def isInfiniteLoop(map, obstaclePosition, direction, position) :
    mapCopy = np.copy(map)
    mapCopy[obstaclePosition[0]][obstaclePosition[1]] = '#'
    exit = False
    while not exit :
        position, direction = moveToObstacle(position, mapCopy, direction)
        if (position[0] + direction[0] == -1 or position[0] + direction[0] == len(map[0]) or position[1] + direction[1] == -1 or position[1] + direction[1] == len(map[1])) :
            return False
        if [position, direction] in stopPositionsDirections :
            return True
        else :
            stopPositionsDirections.append([position, direction])
        direction = changeDirection(direction)

for i in range (len(map[0])) :
    for j in range (len(map[1])) :
        if map[i][j] == '#' or map[i][j] == '^' :
            continue
        stopPositionsDirections = []
        obstaclePosition = [i, j]
        position = initialPosition
        direction = initialDirection
        if isInfiniteLoop(map, obstaclePosition, direction, position) :
            total_2 += 1


print("Total part 2: ", total_2)