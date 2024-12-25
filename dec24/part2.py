lines = []
with open("dec24/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())

total = 0

starters = False

bits = {}

ops = []

wireswaps = [("kmb", "z10"), ("tvp", "z15"), ("dpg", "z25"), ("vdk", "mmf")]

for ind, line in enumerate(lines):
    newline = line
    for ws in wireswaps:
        if ws[0] in line[13:]:
            newline = line.replace(ws[0], ws[1])
        elif ws[1] in line[13:]:
            newline = line.replace(ws[1], ws[0])

    
    if line == "":
        starters = True
    else:
        if not starters:
            bits[newline[:3]] = int(newline[5])
        else:
            ops.append(newline)
            
    pass

renamed = []

def renamewire(ogname, newname):
    for insind, op in enumerate(ops):
        ops[insind] = op.replace(ogname, newname)
    renamed.append((newname, ogname))

while len(ops) > 0:
    outputs = {}
    i = 0
    while i < len(ops):
        op = ops[i]
        args = op.split()
        if args[0] in bits and args[2] in bits:
            
            operation = {"AND": "&", "OR":"|", "XOR":"^"}[args[1]]
            renamebit = f"{args[0]}{operation}{args[2]}>{args[4]}"
            ops.pop(i)
            i -= 1
            #naming the r wires
            if renamebit[0] == "x" and renamebit[4] == "y" and int(renamebit[1:3]) == int(renamebit[5:7]) and \
                renamebit[3] == "^":
                newname = f'r{renamebit[1:3]}'
                renamewire(renamebit[8:11], newname)
                pass
            elif renamebit[0] == "y" and renamebit[4] == "x" and int(renamebit[1:3]) == int(renamebit[5:7]) and \
                renamebit[3] == "^":
                newname = f'r{renamebit[1:3]}'
                renamewire(renamebit[8:11], newname)
                pass

            #naming the a wires
            elif renamebit[0] == "x" and renamebit[4] == "y" and int(renamebit[1:3]) == int(renamebit[5:7]) and \
                renamebit[3] == "&":
                newname = f'a{renamebit[1:3]}'
                if newname == "a00": newname = "c00"
                renamewire(renamebit[8:11], newname)
                pass
            elif renamebit[0] == "y" and renamebit[4] == "x" and int(renamebit[1:3]) == int(renamebit[5:7]) and \
                renamebit[3] == "&":
                newname = f'a{renamebit[1:3]}'
                if newname == "a00": newname = "c00"
                renamewire(renamebit[8:11], newname)
                pass

            #naming the b wires
            elif renamebit[0] == "c" and renamebit[4] == "r" and int(renamebit[1:3]) + 1 == int(renamebit[5:7]) and \
                renamebit[3] == "&":
                newname = f'b{renamebit[5:7]}'
                renamewire(renamebit[8:11], newname)
                pass

            elif renamebit[0] == "r" and renamebit[4] == "c" and int(renamebit[1:3]) - 1 == int(renamebit[5:7]) and \
                renamebit[3] == "&":
                newname = f'b{renamebit[1:3]}'
                renamewire(renamebit[8:11], newname)
                pass

            #checking names of the z wires
            elif renamebit[0] == "r" and renamebit[4] == "c" and int(renamebit[1:3]) - 1 == int(renamebit[5:7]) and \
                renamebit[3] == "^" and renamebit[8:11] == f'z{renamebit[1:3]}':
                newname = f'z{renamebit[1:3]}'
                pass

            elif renamebit[0] == "c" and renamebit[4] == "r" and int(renamebit[1:3]) + 1 == int(renamebit[5:7]) and \
                renamebit[3] == "^" and renamebit[8:11] == f'z{renamebit[5:7]}':
                newname = f'z{renamebit[1:3]}'
                pass

            #naming the c wires
            elif renamebit[0] == "b" and renamebit[4] == "a" and int(renamebit[1:3]) == int(renamebit[5:7]) and \
                renamebit[3] == "|":
                newname = f'c{renamebit[1:3]}'
                renamewire(renamebit[8:11], newname)
                pass

            elif renamebit[0] == "a" and renamebit[4] == "b" and int(renamebit[1:3]) == int(renamebit[5:7]) and \
                renamebit[3] == "|":
                newname = f'c{renamebit[1:3]}'
                renamewire(renamebit[8:11], newname)
                pass
            
            if args[1] == "AND":
                outputs[newname] = int(bits[args[0]]) & int(bits[args[2]])
                pass
            elif args[1] == "OR":
                outputs[newname] = int(bits[args[0]]) | int(bits[args[2]])
                pass
            elif args[1] == "XOR":
                outputs[newname] = int(bits[args[0]]) ^ int(bits[args[2]])
                pass
            print(renamebit[:8] + newname)
            
        i += 1
            
            
    for o in outputs.keys():
        bits[o] = outputs[o]

for k in bits.keys():
    if k[0] == "z":
        total += 2 ** int(k[1:]) * bits[k]

    
#print("\n\n".join([str(i) for i in layers]))
print(bin(total))
print(total)
finalswaps = []
for ws in wireswaps:
    finalswaps += list(ws)
finalswaps.sort()
print(",".join(finalswaps))
