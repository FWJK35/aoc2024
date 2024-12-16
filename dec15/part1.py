lines = []
with open("dec15/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())

grid = []
ind = 0
line = lines[ind]
while line != "":
    line = lines[ind]
    grid.append([c for c in line])
    ind += 1
ind += 0
instructions = []
dirchars = [">", "^", "<", "v"]
dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
while ind < len(lines):
    line = lines[ind]
    for c in line:
        instructions.append(dirchars.index(c))
    ind += 1


total = 0
pos = (0, 0)
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == "@":
            pos = (x, y)
            grid[y][x] = "."
        pass
for y, row in enumerate(grid):
    print("".join(row))
for ins in instructions:
    dir = dirs[ins]
    newpos = (pos[0] + dir[0], pos[1] + dir[1])
    if grid[newpos[1]][newpos[0]] == ".":
        pos = newpos
    elif grid[newpos[1]][newpos[0]] == "#":
        pass
    else:
        topush = 1
        check = (pos[0] + dir[0] * topush, pos[1] + dir[1] * topush)
        while grid[check[1]][check[0]] == "O":
            topush += 1
            check = (pos[0] + dir[0] * topush, pos[1] + dir[1] * topush)


        if grid[check[1]][check[0]] == "#":
            pass
        else:
            grid[check[1]][check[0]] = "O"
            grid[newpos[1]][newpos[0]] = "."
            pos = newpos
    # for y, row in enumerate(grid):
    #     print("".join(row))


for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == "O":
            total += y * 100 + x


print(total)
