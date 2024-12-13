lines = []
with open("dec12/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())

maps = []
regs = []
total = 0
for ind, line in enumerate(lines):
    maps.append([c for c in line])
    pass

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = set()
for y, row in enumerate(maps):
    for x, val in enumerate(row):
        #new region
        if (x, y) not in visited:
            queue = [(x, y)]
            thisreg = set([(x, y)])
            while len(queue) > 0:
                movingfrom = queue.pop(0)
                for dir in dirs:
                    newpos = (movingfrom[0] + dir[0], movingfrom[1] + dir[1])
                    if 0 <= newpos[1] < len(maps) and 0 <= newpos[0] < len(maps[0]):
                        if maps[newpos[1]][newpos[0]] == val and newpos not in visited:
                            visited.add(newpos)
                            thisreg.add(newpos)
                            queue.append(newpos)
            regs.append(thisreg)
print(regs)
for reg in regs:
    area = len(reg)
    perim = 4 * area
    name = ""
    for cell in reg:
        if name == "":
            name = maps[cell[1]][cell[0]]
        for dir in dirs:
            if (cell[0] + dir[0], cell[1] + dir[1]) in reg:
                perim -= 1
    total += area * perim
    a = set()
    print(name, area, perim)


print(total)
