with open("6.txt", "r") as f: f = f.read().splitlines()
new_lst = list(map(list, zip(*[list(line) for line in f])))
newOverall, temp, total = list(), list(), 0
for lst in new_lst:
    if lst != [" "] * 5: temp.append(lst)
    else:
        newOverall.append(temp)
        temp = []
newOverall.append(temp)
        
for lst in newOverall:
    operator, nums = bool(), []
    for lsts in lst:
        temp_num = str()
        for char in lsts:
            if char == "*": operator = True
            elif char == "+": operator = False
            else: temp_num += char
        nums.append(int(temp_num.strip()))
    if operator == False: total += sum(nums)
    else:
        temp_total = 1
        for num in nums: temp_total *= num
        total += temp_total
print(total)