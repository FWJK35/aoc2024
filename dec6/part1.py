lines = []
with open("dec6/sample.txt", "r") as file:
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
visited = []
facing = 0
dirs = [(0,-1), (1, 0), (0,1), (1,0)]
while True:
    while (gx + dirs[facing][0], gy + dirs[facing][1]) in obstacles:
        facing = (facing + 1) % 4
    
    gx += dirs[facing][0]
    gy += dirs[facing][1]
    print(gx, gy, facing)
    if gx < 0 or gx >= len(lines[0]) or gy < 0 or gy >= len(lines):
        break
    else:
        if (gx, gy) not in visited:
            visited.append((gx, gy))
            total += 1

print(total)