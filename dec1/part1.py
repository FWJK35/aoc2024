lines = []
with open("dec1/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())

a = []
b = []
for line in lines:
    num1, num2 = (int(i) for i in line.split())
    a.append(num1)
    b.append(num2)

a.sort()
b.sort()
tot = 0
for i in range(len(a)):
    tot += abs(a[i] - b[i])
print(tot)