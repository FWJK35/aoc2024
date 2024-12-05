lines = []
with open("dec4/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())

total = 0

for x in range(1, len(lines) - 1):
    for y in range(1, len(lines[x]) - 1):
        masses = ["MAS", "SAM"]
        for m in range(0, 2):
            for s in range(0, 2):
                isxmas = True
                for i in range(-1, 2):
                    if lines[x+i][y+i] != masses[m][i+1]:
                        isxmas = False
                for i in range(-1, 2):
                    if lines[x+i][y-i] != masses[s][i+1]:
                        isxmas = False
                if isxmas: total += 1
                        


print(total)