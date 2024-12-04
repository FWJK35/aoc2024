lines = []
with open("dec3/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())

total = 0
enabled = True
for line in lines:
    for c in range(len(line)-4):
        if line[c:c+4] == "mul(":
            test = line[c+4:c+12]
            for maybe in range(len(test)):
                if test[maybe] == ")":
                    check = test[:maybe]
                    try:
                        nums = [int(i) for i in check.split(",")]
                        if len(nums) == 2 and enabled:
                            if nums[0] < 1000 and nums[1] < 1000:
                                total += nums[0] * nums[1]
                    except Exception:
                        break
        if line[c:c+4] == "do()":
            enabled = True
        if line[c:c+7] == "don't()":
            enabled = False
            
print(total)
