lines = []
with open("dec3/input.txt", "r") as file:
    for line in file.readlines():
        lines.append(line.strip())

total = 0
for line in lines:
    for test in line.split("mul("):
        for maybe in range(len(test)):
            if test[maybe] == ")":
                check = test[:maybe]
                try:
                    nums = [int(i) for i in check.split(",")]
                    if len(nums) == 2:
                        if nums[0] < 1000 and nums[1] < 1000:
                            total += nums[0] * nums[1]
                except Exception:
                    break
        

            
print(total)
