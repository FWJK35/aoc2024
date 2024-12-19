lines = []
with open("dec18/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())

total = 0
size = 71
grid = [[0 for i in range(size)] for j in range(size)]
bytes = []
for ind, line in enumerate(lines):
    x, y = (int(i) for i in line.split(","))
    bytes.append((x, y))

for b, byte in enumerate(bytes):
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c != -1:
                grid[y][x] = 0
    grid[byte[1]][byte[0]] = -1
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
    print(b)
    if grid[size - 1][size - 1] == 0:
        print(byte)
        break

