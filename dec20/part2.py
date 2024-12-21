lines = []
with open("dec20/input.txt", "r") as file:
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
            grid[y][x] = "."
        if c == "E":
            end = (x, y)
            grid[y][x] = "."

queue = [start]
visited = set(queue)
dist = 0
last = 1
gridtimes = [[-1 for x in range(len(grid[0]))] for y in range(len(grid))]
while len(queue) > 0:
    movingfrom = queue.pop(0)
    gridtimes[movingfrom[1]][movingfrom[0]] = dist
    last -= 1
    for md in dirs:
        newpos = (movingfrom[0] + md[0], movingfrom[1] + md[1])
        if newpos not in visited and grid[newpos[1]][newpos[0]] == ".":
            visited.add(newpos)
            queue.append(newpos)
    if last == 0:
        dist += 1
        last = len(queue)
slowtime = gridtimes[end[1]][end[0]]
print(slowtime)
path = [end]
while gridtimes[path[-1][1]][path[-1][0]] > 0:
    movingfrom = path[-1]
    for md in dirs:
        newpos = (movingfrom[0] + md[0], movingfrom[1] + md[1])
        if gridtimes[newpos[1]][newpos[0]] == gridtimes[movingfrom[1]][movingfrom[0]] - 1:
            path.append(newpos)

for row in gridtimes:
    print("".join([f'{t:02d} ' for t in row]))

timesavers = {}
for cs in range(len(path)):
    for ce in range(cs + 1, len(path)):
        cspos = path[cs]
        cepos = path[ce]
        separation = abs(cepos[0] - cspos[0]) + abs(cepos[1] - cspos[1])
        if separation <= 20:
            timesaved = ce - cs - separation
            if timesaved > 0:
                timesavers.setdefault(timesaved, 0)
                timesavers[timesaved] += 1
                if timesaved >= 100:
                    total += 1
    if cs % 100 == 0:
        print(cs/len(path))

tskeys = list(timesavers.keys())
tskeys.sort()
for ts in tskeys:
    if ts >= 50:
        print(ts, timesavers[ts])


print(total)
