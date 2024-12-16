lines = []
with open("dec15/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())

grid = []
ind = 0
line = lines[ind]
while line != "":
    line = lines[ind]
    row = ""
    for c in line:
        if c == "@":
            row += "@."
        if c == "#":
            row += "##"
        if c == "O":
            row += "[]"
        if c == ".":
            row += ".."
    ind += 1
    grid.append([c for c in row])
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
        #normal horizontal movement
        if ins % 2 == 0:

            topush = 1
            check = (pos[0] + dir[0] * topush, pos[1] + dir[1] * topush)
            while grid[check[1]][check[0]] == "[" or grid[check[1]][check[0]] == "]":
                topush += 1
                check = (pos[0] + dir[0] * topush, pos[1] + dir[1] * topush)
            if grid[check[1]][check[0]] == "#":
                pass
            else:
                for pushed in range(topush, 0, -1):
                    check = (pos[0] + dir[0] * pushed, pos[1] + dir[1] * pushed)
                    newspot = (pos[0] + dir[0] * (pushed - 1), pos[1] + dir[1] * (pushed - 1))
                    grid[check[1]][check[0]] = grid[newspot[1]][newspot[0]]
                grid[newpos[1]][newpos[0]] = "."
                pos = newpos
        
        else:
            topush = 0
            check = (pos[0] + dir[0], pos[1] + dir[1])
            tomove = {"[":1, "]":-1}
            checks = set()
            checks.add(check)
            checks.add((check[0] + tomove[grid[check[1]][check[0]]], check[1]))
            canmove = True
            nomorepush = False
            while not nomorepush and canmove:
                topush += 1
                newchecks = set()
                for front in checks:
                    if grid[front[1] + dir[1]][front[0]] == "#":
                        canmove = False
                        break
                    if grid[front[1] + dir[1]][front[0]] == "[" or grid[front[1] + dir[1]][front[0]] == "]":
                        newchecks.add((front[0], front[1] + dir[1]))
                        newchecks.add((front[0] + tomove[grid[front[1] + dir[1]][front[0]]], front[1] + dir[1]))
                checks |= newchecks
                nomorepush = True
                for row in checks:
                    if row[1] == pos[1] + topush * dir[1]:
                        if grid[row[1] + dir[1]][row[0]] == "[" or grid[row[1] + dir[1]][row[0]] == "]":
                            nomorepush = False
                            break
            if canmove:
                for i in range(topush, 0, -1):
                    for tomove in checks:
                        if tomove[1] == pos[1] + i * dir[1]:
                            grid[tomove[1] + dir[1]][tomove[0]] = grid[tomove[1]][tomove[0]]
                            grid[tomove[1]][tomove[0]] = "."
                pos = newpos
    # print(dirchars[ins])
    # grid[pos[1]][pos[0]] = "@"
    # for y, row in enumerate(grid):
    #         print("".join(row))
    # grid[pos[1]][pos[0]] = "."
    
    pass


for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == "[":
            total += y * 100 + x


print(total)
