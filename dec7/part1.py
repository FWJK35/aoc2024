lines = []
with open("dec7/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())


total = 0

for ind, line in enumerate(lines):
    prod = int(line.split(":")[0])
    nums = [int(i) for i in line.split(":")[1].strip().split()]
    print(prod, nums)
    for t in range(2**(len(nums)-1)):
        ops = "0" * (len(nums) - len(bin(t))+1) + bin(t)[2:]

        res = nums[0]
        for i, op in enumerate(ops):
            if op == "0":
                res += nums[i+1]
            else:
                res *= nums[i+1]
        if res == prod:
            print(prod)
            total += prod
            break
    pass
print(total)
