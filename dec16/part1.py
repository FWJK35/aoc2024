lines = []
with open("dec16/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())

total = 0
grid = []
for ind, line in enumerate(lines):
    grid.append([c for c in line])
    pass

start = (0, 0)
end = (0, 0)
dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]

for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == "S":
            start = (x, y)
        if c == "E":
            end = (x, y)

lowest = [[[-1 for f in range(4)] for x in range(len(grid[0]))] for y in range(len(grid))]

queue = []
lowest[start[1]][start[0]][0] = 0
queue.append((start[0], start[1], 0))

def movefrom(moving, newpos, scorechange):
    if grid[newpos[1]][newpos[0]] != "#":
        if lowest[newpos[1]][newpos[0]][newpos[2]] == -1 or lowest[moving[1]][moving[0]][moving[2]] + scorechange < lowest[newpos[1]][newpos[0]][newpos[2]]:
            lowest[newpos[1]][newpos[0]][newpos[2]] = lowest[moving[1]][moving[0]][moving[2]] + scorechange
            return newpos
    return False
print(queue)

while len(queue) > 0:
    moving = queue.pop(0)
    rightturn = movefrom(moving, (moving[0], moving[1], (moving[2] + 1) % 4), 1000)
    leftturn = movefrom(moving, (moving[0], moving[1], (moving[2] - 1) % 4), 1000)
    movefwd = movefrom(moving, (moving[0] + dirs[moving[2]][0], moving[1] + dirs[moving[2]][1], moving[2]), 1)
    if rightturn:
        queue.append(rightturn)
    if leftturn:
        queue.append(leftturn)
    if movefwd:
        queue.append(movefwd)
print(lowest[end[1]][end[0]])
total = min(lowest[end[1]][end[0]])
    


print(total)
