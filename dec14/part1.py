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
for t in range(100):
    for r in robots:
        r[0] = (r[0] + r[2]) % w
        r[1] = (r[1] + r[3]) % h
q1 = 0
q2 = 0
q3 = 0
q4 = 0
for r in robots:
    if r[0] > w // 2 and r[1] > h // 2:
        q1 += 1
    if r[0] < w // 2 and r[1] > h // 2:
        q2 += 1
    if r[0] < w // 2 and r[1] < h // 2:
        q3 += 1
    if r[0] > w // 2 and r[1] < h // 2:
        q4 += 1
total = q1 * q2 * q3 * q4

print(total)
