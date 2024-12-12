lines = open('/Users/architwankhade/Downloads/AdventOfCode/2024/day10/input.txt').read().splitlines()

from collections import deque

m = [list(map(int, list(line))) for line in lines]
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def inbound(r, c):
    return 0 <= r < len(m) and 0 <= c < len(m[0])

def p1(m, end):
    visited = set()
    D = deque([end])
    n = 0

    while D:
        i, j = D.pop()

        if (i, j) in visited: continue
        if m[i][j] == 0: n += 1

        visited.add((i, j))
        for d in DIRS:
            di, dj = i + d[0], j + d[1]
            if inbound(di, dj) and m[di][dj] == (m[i][j] - 1):
                D.append((di, dj))
            
    return n

r = {}
def p2(m, end):
    i, j = end
    if m[i][j] == 0: return 1

    splits = 0
    for d in DIRS:
        di, dj = i + d[0], j + d[1]
        if inbound(di, dj) and m[di][dj] == (m[i][j] - 1):
            splits += p2(m, (di, dj))
    r[end] = splits
    return splits

s, l = 0, 0

for i in range(len(m)):
    for j in range(len(m[i])):
            if m[i][j] == 9:
                s += p1(m, (i, j))
                l += p2(m, (i, j))

print(s, l)
