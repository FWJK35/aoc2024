lines = []
with open("dec14/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())
h = 103
w = 101
total = 0
robots = [] 
a = ""
for ind, line in enumerate(lines):
    rx = int(line[line.index("p") + 2: line.index(",")])
    ry = int(line[line.index(",") + 1: line.index("v=")])
    vx, vy = [int(i) for i in line[line.index("v=") + 2:].split(",")]
    robots.append([rx, ry, vx, vy])
    pass

tx = 0
steps = 0
while True:
    ty = round((103 * tx - 49) / 101, 5)
    if int(ty) == ty:
        steps = ty * 101 + 98
        break
    tx += 1
    print(tx)
t = 0
while t < steps:
    for r in robots:
        r[0] = (r[0] + r[2]) % w
        r[1] = (r[1] + r[3]) % h
    t += 1
    print(t)
for y in range(h):
        line = ""
        for x in range(w):
            count = 0
            for r in robots:
                if r[0] == x and r[1] == y:
                    count += 1
                    break
            if count > 0:
                line += "XXX"
            else:
                line += "   "
        print(line)


print(t)
