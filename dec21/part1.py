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

for code in codes:
    r1presses = set()
    r1presses.add("")
    pos = (2, 3)
    for c in code:
        diff = (buttons[c][0] - pos[0], buttons[c][1] - pos[1])
        xchar = "<" if diff[0] < 0 else ">" if diff[0] > 0 else ""
        ychar = "^" if diff[1] < 0 else "v" if diff[1] > 0 else ""
        xfirst = xchar * abs(diff[0]) + ychar * abs(diff[1]) + "A"
        yfirst = ychar * abs(diff[1]) + xchar * abs(diff[0]) + "A"
        newr1presses = set()
        if not(pos[0] + diff[0] == 0 and pos[1] == 3):
            for press in r1presses:
                newr1presses.add(press + xfirst)
        if not(pos[1] + diff[1] == 3 and pos[0] == 0):
            for press in r1presses:
                newr1presses.add(press + yfirst)
        r1presses = newr1presses
        pos = (buttons[c][0], buttons[c][1])

    r2presses = set()
    for r1p in r1presses:
        thispresses = set()
        thispresses.add("")
        pos = (2, 0)
        for b in r1p:
            diff = (dirbuttons[b][0] - pos[0], dirbuttons[b][1] - pos[1])
            xchar = "<" if diff[0] < 0 else ">" if diff[0] > 0 else ""
            ychar = "^" if diff[1] < 0 else "v" if diff[1] > 0 else ""
            xfirst = xchar * abs(diff[0]) + ychar * abs(diff[1]) + "A"
            yfirst = ychar * abs(diff[1]) + xchar * abs(diff[0]) + "A"
            newthispresses = set()
            if not(pos[0] + diff[0] == 0 and pos[1] == 0):
                for press in thispresses:
                    newthispresses.add(press + xfirst)
            if not(pos[1] + diff[1] == 0 and pos[0] == 0):
                for press in thispresses:
                    newthispresses.add(press + yfirst)
            thispresses = newthispresses
            pos = (dirbuttons[b][0], dirbuttons[b][1])
        r2presses |= thispresses


    r3presses = set()
    for r2p in r2presses:
        thispresses = set()
        thispresses.add("")
        pos = (2, 0)
        for b in r2p:
            diff = (dirbuttons[b][0] - pos[0], dirbuttons[b][1] - pos[1])
            xchar = "<" if diff[0] < 0 else ">" if diff[0] > 0 else ""
            ychar = "^" if diff[1] < 0 else "v" if diff[1] > 0 else ""
            xfirst = xchar * abs(diff[0]) + ychar * abs(diff[1]) + "A"
            yfirst = ychar * abs(diff[1]) + xchar * abs(diff[0]) + "A"
            newthispresses = set()
            if not(pos[0] + diff[0] == 0 and pos[1] == 0):
                for press in thispresses:
                    newthispresses.add(press + xfirst)
            if not(pos[1] + diff[1] == 0 and pos[0] == 0):
                for press in thispresses:
                    newthispresses.add(press + yfirst)
            thispresses = newthispresses
            pos = (dirbuttons[b][0], dirbuttons[b][1])
        r3presses |= thispresses

    total += min([len(seq) for seq in r3presses]) * int(code[:3])

            
    

print(total)
