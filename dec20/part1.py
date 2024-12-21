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
while len(queue) > 0:
    movingfrom = queue.pop(0)
    if movingfrom == end:
        break
    last -= 1
    for md in dirs:
        newpos = (movingfrom[0] + md[0], movingfrom[1] + md[1])
        if newpos not in visited and grid[newpos[1]][newpos[0]] == ".":
            visited.add(newpos)
            queue.append(newpos)
    if last == 0:
        dist += 1
        last = len(queue)
slowtime = dist
print(slowtime)
timesavers = {}
for cheatstart in range(len(grid) * len(grid[0])):
    cheatpos = [(cheatstart % len(grid[0]), cheatstart // len(grid[0]))]
    #cheatpos.append((cheatpos[0][0] + cheatdir[0], cheatpos[0][1] + cheatdir[1]))
    changed = []
    for c in cheatpos:
        if 0 <= c[0] < len(grid[0]) and 0 <= c[1] < len(grid):
            if grid[c[1]][c[0]] == "#":
                grid[c[1]][c[0]] = "."
                changed.append(c)
    queue = [start]
    visited = set(queue)
    dist = 0
    last = 1
    while len(queue) > 0:
        movingfrom = queue.pop(0)
        if movingfrom == end:
            break
        last -= 1
        for md in dirs:
            newpos = (movingfrom[0] + md[0], movingfrom[1] + md[1])
            if 0 <= newpos[0] < len(grid[0]) and 0 <= newpos[1] < len(grid):
                if newpos not in visited and grid[newpos[1]][newpos[0]] == ".":
                    visited.add(newpos)
                    queue.append(newpos)
        if last == 0:
            dist += 1
            last = len(queue)
    timesaved = slowtime - dist
    timesavers.setdefault(timesaved, 0)
    timesavers[timesaved] += 1
    if timesaved >= 100:
        total += 1
    for c in changed:
        grid[c[1]][c[0]] = "#"
    if cheatstart % 100 == 0: print(cheatstart / (141**2))
        

print(timesavers)

print(total)
