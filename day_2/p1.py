with open("2.txt", "r") as f: f = f.readline().split(",")
count = 0
for id_range in f:
    temp = id_range.split("-")
    for j in range(int(temp[0]), int(temp[1]) + 1):
        if len(str(j)) % 2 == 0 and str(j)[0:int(len(str(j))/2)] == str(j)[int(len(str(j))/2):]: count += j
print(count)