with open("6.txt", "r") as f: f = f.read().splitlines()
overall_lst = []

for i in range(len(f)):
    temp = []
    for char in f[i]: temp.append(char)
    overall_lst.append(temp)

new_lst = []
for k in range(len(overall_lst[0])):
    temp_lst = []
    for lst in overall_lst: temp_lst.append(lst[k])
    new_lst.append(temp_lst)

overall, temp2, total = [], [], 0
for lst in new_lst:
    if lst != [" "] * 5: temp2.append(lst)
    else:
        overall.append(temp2)
        temp2  = []
overall.append(temp2)
        
for lst in overall:
    operator = True # True = *
    nums = []
    for lsts in lst:
        temp_num = ""
        for char in lsts:
            if char == "*": operator = True
            elif char == "+": operator = False
            else: temp_num += char
        nums.append(int(temp_num.strip()))
    
    if operator == False: total += sum(nums)
    else:
        result = 1
        for num in nums:
            result *= num
        total += result     
print(total)