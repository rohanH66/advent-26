with open("5.txt", "r") as f: f = f.read().splitlines()
ranges, ids, merged, range_check, count = list(), list(), list(), True, 0
for line in f:
    if line == "":
        range_check = False
        continue
    if range_check: ranges.append((int(line.split("-")[0]), int(line.split("-")[1])))
    else: ids.append(int(line))

for first, last in sorted(ranges):
    if not merged or first > merged[-1][1] + 1: merged.append([first, last])  
    else: merged[-1][1] = max(merged[-1][1], last)

for id in ids:
    for a, b in merged:
        if a <= id <= b:
            count += 1
            break
print(count)