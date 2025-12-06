with open("6.txt", "r") as f: f = f.read().splitlines()
overall_lst = list()
for line in f: overall_lst.append(line.split())
    
new_lst, total= list(), 0
for i in range(len(overall_lst[0])):
    temp = list()
    for j in range(0, 5): temp.append(overall_lst[j][i])
    new_lst.append(temp)

for lst in new_lst:
    if lst[4] == "*": total += (int(lst[0]) * int(lst[1]) * int(lst[2]) * int(lst[3]))
    if lst[4] == "+": total += (int(lst[0]) + int(lst[1]) + int(lst[2]) + int(lst[3]))
    
print(total)