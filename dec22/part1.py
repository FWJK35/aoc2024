lines = []
with open("dec22/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())

total = 0
nums = []
for ind, line in enumerate(lines):
    nums.append(int(line))
    pass

for num in nums:
    n = num
    for s in range(2000):
        n ^= n * 64
        n %= 16777216
        n ^= n // 32
        n %= 16777216
        n ^= n * 2048
        n %= 16777216
    total += n
    

print(total)
