lines = []
with open("dec24/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())

total = 0

starters = False

bits = {}

ops = []

for ind, line in enumerate(lines):
    if line == "":
        starters = True
    else:
        if not starters:
            bits[line[:3]] = int(line[5])
        else:
            ops.append(line)
            
    pass

while len(ops) > 0:
    for i, op in enumerate(ops):
        args = op.split()
        if args[0] in bits and args[2] in bits:
            if args[1] == "AND":
                bits[args[4]] = int(bits[args[0]]) & int(bits[args[2]])
                pass
            elif args[1] == "OR":
                bits[args[4]] = int(bits[args[0]]) | int(bits[args[2]])
                pass
            elif args[1] == "XOR":
                bits[args[4]] = int(bits[args[0]]) ^ int(bits[args[2]])
                pass

            ops.pop(i)
            break


for k in bits.keys():
    if k[0] == "z":
        total += 2 ** int(k[1:]) * bits[k]

print(bin(total))
print(total)
