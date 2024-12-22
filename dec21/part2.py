lines = []
with open("dec21/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())

total = 0

buttons = {}
for b in range(9):
    buttons[f'{b+1}'] = (b % 3, 2 - (b // 3))
buttons["0"] = (1, 3)
buttons["A"] = (2, 3)

dirbuttons = {"^":(1, 0), "A":(2, 0), "<":(0, 1), "v":(1, 1), ">":(2, 1)}
print(buttons)

codes = []
for ind, line in enumerate(lines):
    codes.append(line)
    pass

def getpressseq(start, topress):
    diff = (dirbuttons[topress][0] - dirbuttons[start][0], dirbuttons[topress][1] - dirbuttons[start][1])
    xchar = "<" if diff[0] < 0 else ">" if diff[0] > 0 else ""
    ychar = "^" if diff[1] < 0 else "v" if diff[1] > 0 else ""
    xfirst = xchar * abs(diff[0]) + ychar * abs(diff[1]) + "A"
    yfirst = ychar * abs(diff[1]) + xchar * abs(diff[0]) + "A"
    poss = []
    pos = dirbuttons[start]
    if not(pos[0] + diff[0] == 0 and pos[1] == 0):
        poss.append(xfirst)
    if not(pos[1] + diff[1] == 0 and pos[0] == 0):
        if yfirst != xfirst:
            poss.append(yfirst)
    if start + topress == "^>": return yfirst
    if start + topress == "<^": return xfirst

    if start + topress == "Av": return xfirst
    if start + topress == "vA": return yfirst
    return poss[0]


for code in codes:
    presses = set()
    presses.add("")
    pos = (2, 3)
    for c in code:
        diff = (buttons[c][0] - pos[0], buttons[c][1] - pos[1])
        xchar = "<" if diff[0] < 0 else ">" if diff[0] > 0 else ""
        ychar = "^" if diff[1] < 0 else "v" if diff[1] > 0 else ""
        xfirst = xchar * abs(diff[0]) + ychar * abs(diff[1]) + "A"
        yfirst = ychar * abs(diff[1]) + xchar * abs(diff[0]) + "A"
        newpresses = set()
        if not(pos[0] + diff[0] == 0 and pos[1] == 3):
            for press in presses:
                newpresses.add(press + xfirst)
        if not(pos[1] + diff[1] == 3 and pos[0] == 0):
            for press in presses:
                newpresses.add(press + yfirst)
        presses = newpresses
        pos = (buttons[c][0], buttons[c][1])

    presscounts = []
    for seq in presses:
        movescombos = {}
        prevb = "A"
        for nextb in seq:
            thismove = prevb + nextb
            movescombos.setdefault(thismove, 0)
            movescombos[thismove] += 1
            prevb = nextb
        
        for r in range(25):
            nextmovescombos = {}
            for mc in movescombos:
                mcseqlens = {}
                mcseq = getpressseq(mc[0], mc[1])
                    
                prevb = "A"
                for nextb in mcseq:
                    thismove = prevb + nextb
                    nextmovescombos.setdefault(thismove, 0)
                    nextmovescombos[thismove] += movescombos[mc]
                    prevb = nextb
            movescombos = nextmovescombos
        presscounts.append(sum(movescombos.values()))


    total += min(presscounts) * int(code[:3])


    

print(total)
