lines = []
with open("dec17/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())

total = 0
a = int(lines[0][lines[0].index(":") + 2:])
b = int(lines[1][lines[1].index(":") + 2:])
c = int(lines[2][lines[2].index(":") + 2:])
ins = [int(i) for i in lines[4][lines[4].index(":") + 2:].split(",")]

def runbits(inita, numbits):
    result = [-1 for i in range(numbits)]
    a = inita

    for outbit in range(numbits):

        b = a % 8
        b ^= 2
        c = a // (2**b)
        b ^= 7
        b ^= c
        result[outbit] = b % 8
        a //= 8
        if a == 0:
            break
    return tuple(result)

bitsfound = []
foundcount = 0
currentnums = [0]

while foundcount < len(ins):
    newnums = []
    for currentnum in currentnums:
        foundbits = []
        
        binf = ""
        remf = currentnum
        while len(binf) < (foundcount + 1) * 3:
            binf = str(remf % 2) + binf
            remf //= 2
        print("testing:", currentnum, binf)

        for tbits in range(8):
            thisresult = runbits(tbits + currentnum * 8, foundcount + 1)
            for check in range(foundcount + 1):
                insind = len(ins) - foundcount - 1 + check
                if thisresult[check] != -1 and insind < len(ins) and thisresult[check] != ins[insind]:
                    break
            else:
                foundbits.append(tbits)

        print(len(foundbits))
        for f in foundbits:
            binf = ""
            remf = f + currentnum * 8
            while len(binf) < (foundcount + 1) * 3:
                binf = str(remf % 2) + binf
                remf //= 2
            print(f, binf, str(runbits(f + currentnum * 8, foundcount + 1)))
            newnums.append(currentnum * 8 + f)

    currentnums = newnums
    foundcount += 1
print(currentnums)
print(min(currentnums))
        

