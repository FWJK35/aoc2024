lines = []
with open("dec22/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())

total = 0
nums = []
for ind, line in enumerate(lines):
    nums.append(int(line))
    pass

changes = []
changevals = {}

for c in range(21**4):
    changes = []
    cc = c
    while len(changes) < 4:
        changes.append(cc % 21 - 10)
        cc //= 21
    cmax = 0
    cmin = 0
    current = 0
    for d in changes:
        current += d
        cmax = max(cmax, current)
        cmin = min(cmin, current)
    if cmax - cmin < 10:
        changevals[tuple(changes)] = 0
print(len(changevals))

print("changes initialized")
for ind, num in enumerate(nums):
    n = num
    prevprice = 0
    currentchange = []
    for s in range(2000):
        n ^= n * 64
        n %= 16777216
        n ^= n // 32
        n %= 16777216
        n ^= n * 2048
        n %= 16777216
        price = n % 10

        if s != 0:
            pricechange = price - prevprice
            currentchange.append(pricechange)
            if len(currentchange) > 4:
                currentchange.pop(0)
            if len(currentchange) == 4 and changevals[tuple(currentchange)] >= 0:
                changevals[tuple(currentchange)] = -(changevals[tuple(currentchange)] + price)
        prevprice = price
    for cv in changevals.keys():
        if changevals[cv] < 0:
            changevals[cv] *= -1

        #print("0" * (26 - len(bin(n))) + bin(n)[2:])
maxprofit = max(changevals.values())
for cv in changevals.keys():
    if changevals[cv] == maxprofit:
        print(cv)
print(maxprofit)
