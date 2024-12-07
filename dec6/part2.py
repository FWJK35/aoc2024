lines = []
with open("dec6/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())


total = 0
obstacles = []
gx, gy = 0, 0
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "#":
            obstacles.append((x, y))
        if c == "^":
            gx, gy = x, y

    pass
print(obstacles)
print(gx, gy)
visited = [(gx, gy)]
visdirs = [(gx, gy, 0)]
boxes = []
facing = 0
dirs = [(0,-1), (1, 0), (0,1), (-1,0)]
while True:
    turns = 0
    while (gx + dirs[facing][0], gy + dirs[facing][1]) in obstacles:
        facing = (facing + 1) % 4
        visdirs.append((gx, gy, facing))
    
    gx += dirs[facing][0]
    gy += dirs[facing][1]
    if gx < 0 or gx >= len(lines[0]) or gy < 0 or gy >= len(lines):
        break
    else:
        visdirs.append((gx, gy, facing))
    
for index, path in enumerate(visdirs):
    gx = path[0]
    gy = path[1]
    facing = path[2]
    if (gx + dirs[path[2]][0], gy + dirs[path[2]][1]) not in boxes and\
          (gx + dirs[path[2]][0], gy + dirs[path[2]][1]) not in visited:
        obstacles.append((gx + dirs[path[2]][0], gy + dirs[path[2]][1]))
        testvisited = [(gx, gy, facing)]
        while True:
            while (gx + dirs[facing][0], gy + dirs[facing][1]) in obstacles:
                testvisited.append((gx, gy, facing))
                facing = (facing + 1) % 4
                

            gx += dirs[facing][0]
            gy += dirs[facing][1]
            
            if gx < 0 or gx >= len(lines[0]) or gy < 0 or gy >= len(lines):
                break
            if (gx, gy, facing) in testvisited:
                total += 1
                boxes.append((path[0] + dirs[path[2]][0], path[1] + dirs[path[2]][1]))
                print(boxes[-1])
                break
            testvisited.append((gx, gy, facing))
        obstacles.pop(-1)
    visited.append((path[0], path[1]))
    if index % 100 == 0: print(index)

print(total)