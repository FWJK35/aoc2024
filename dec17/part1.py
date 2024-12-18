lines = []
with open("dec17/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())

total = 0
a = int(lines[0][lines[0].index(":") + 2:])
b = int(lines[1][lines[1].index(":") + 2:])
c = int(lines[2][lines[2].index(":") + 2:])
ins = [int(i) for i in lines[4][lines[4].index(":") + 2:].split(",")]

def combo(operand):
    if operand < 4:
        return operand
    else:
        return [a, b, c][operand - 4]

pointer = 0
output = []

while pointer < len(ins):
    opcode = ins[pointer]
    operand = ins[pointer + 1]
    match opcode:
        case 0:
            a = a // 2**combo(operand)
            pass
        case 1:
            b = b ^ operand
            pass
        case 2:
            b = combo(operand) % 8
            pass
        case 3:
            if a != 0:
                pointer = operand
                pointer -= 2
            pass
        case 4:
            b = b ^ c
            pass
        case 5:
            output.append(str(combo(operand) % 8))
            pass
        case 6:
            b = a // 2**combo(operand)
            pass
        case 7:
            c = a // 2**combo(operand)
            pass

    pointer += 2
print(output)


print(",".join(output))
