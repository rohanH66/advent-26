with open('1.txt', "r") as f: data = f.read().splitlines()
start, count = 50, 0
for line in data:
    if (start := (start + int(line[1:]) if line[0] == "R" else start - int(line[1:])) % 100) == 0: count += 1
print(count)