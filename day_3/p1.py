with open("3.txt", "r") as f: f = f.read().splitlines()
maxT, total = -1, 0
for line in f:
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            if int(line[i] + line[j]) > maxT: maxT = int(line[i] + line[j])    
    total += maxT
    maxT = -1
print(total)