lines = []
with open("dec18/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())

total = 0
size = 71
grid = [[0 for i in range(size)] for j in range(size)]
for ind, line in enumerate(lines):
    x, y = (int(i) for i in line.split(","))
    if ind < 1024:
        grid[y][x] = -1
    pass

queue = [(0, 0)]
visited = set()
visited.add(queue[0])
dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
while len(queue) > 0:
    movefrom = queue.pop()
    for d in dirs:
        if 0 <= movefrom[1] + d[1] < size and 0 <= movefrom[0] + d[0] < size:
            if grid[movefrom[1] + d[1]][movefrom[0] + d[0]] != -1:
                if grid[movefrom[1] + d[1]][movefrom[0] + d[0]] == 0 or \
                    grid[movefrom[1] + d[1]][movefrom[0] + d[0]] > grid[movefrom[1]][movefrom[0]] + 1:
                    queue.append((movefrom[0] + d[0], movefrom[1] + d[1]))
                    grid[movefrom[1] + d[1]][movefrom[0] + d[0]] = grid[movefrom[1]][movefrom[0]] + 1
                if grid[movefrom[1] + d[1]][movefrom[0] + d[0]] < grid[movefrom[1]][movefrom[0]] - 1:
                    queue.append((movefrom[0] + d[0], movefrom[1] + d[1]))

print(grid[size - 1][size - 1])
