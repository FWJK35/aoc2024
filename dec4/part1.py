lines = []
with open("dec4/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())

total = 0
for line in lines:
    total += line.count("XMAS") + line.count("SAMX")
    pass
horizontal = ["" for i in range(len(lines[0]))]
for line in range(len(lines)):
    for c in range(len(lines[line])):
        horizontal[c]+= lines[line][c]
print(total)

for line in horizontal:
    
    total += line.count("XMAS") + line.count("SAMX")
    pass
print(total)

for x in range(len(lines)):
    for y in range(len(lines[x])):
        xmas = "XMAS"
        isxmas = True
        try:
            for i in range(4):
                if lines[x + i][y + i] != xmas[i]:
                    isxmas = False
                    break
        except Exception:
            isxmas = False
            pass
        if isxmas: 
            print(y, x, "a")
            total += 1

        isxmas = True
        try:
            for i in range(4):
                if y-i < 0:
                    isxmas = False
                    break 
                if lines[x + i][y - i] != xmas[i]:
                    isxmas = False
                    break
        except Exception:
            isxmas = False
            pass
        if isxmas: 
            print(y, x, "b")
            total += 1

        xmas = "SAMX"
        isxmas = True
        try:
            for i in range(4):
                if lines[x + i][y + i] != xmas[i]:
                    isxmas = False
                    break
        except Exception:
            isxmas = False
            pass
        if isxmas: 
            print(y, x, "c")
            total += 1

        isxmas = True
        try:
            for i in range(4):
                if y-i < 0:
                    isxmas = False
                    break 
                if lines[x + i][y - i] != xmas[i]:
                    isxmas = False
                    break
        except Exception:
            isxmas = False
            pass
        if isxmas: 
            print(y, x, "d")
            total += 1

print(total)