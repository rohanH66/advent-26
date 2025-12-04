dirs = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]

with open("4.txt", "r") as f: grid = [list(line) for line in f.read().splitlines()]

rows, cols = len(grid), len(grid[0])

padded = [['.'] * (cols + 2)]
for row in grid: padded.append(['.'] + row + ['.'])
padded.append(['.'] * (cols + 2))

accessible = 0
for r in range(1, rows+1):
    for c in range(1, cols+1):
        if padded[r][c] != "@": continue
        count = 0
        for dx, dy in dirs:
            if padded[r+dx][c+dy] == "@": count += 1
        if count < 4: accessible += 1

print(accessible)