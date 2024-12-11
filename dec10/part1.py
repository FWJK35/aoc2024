lines = []
with open("dec10/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())

total = 0
heights = []
for ind, line in enumerate(lines):
    heights.append([int(i) for i in line])
    pass

levels = {}
for y, line in enumerate(heights):
    for x, h in enumerate(line):
        levels.setdefault(h, [])
        levels[h].append((x, y))
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def movefrom(points, level):
    outpoints = set()
    for p in points:
        for d in dirs:
            if (p[0] + d[0], p[1] + d[1]) in levels[level + 1]:
                outpoints.add((p[0] + d[0], p[1] + d[1]))
    return outpoints

for th in levels[0]:
    points = set()
    points.add(th)
    print(points)
    for step in range(9):
        points = movefrom(points, step)
    print(points, len(points))
    total += len(points)
    


print(heights)
print(total)
