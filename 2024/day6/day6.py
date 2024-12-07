

lines = open('/Users/architwankhade/Downloads/AdventOfCode/2024/day6/input.txt').read().splitlines()

dirs = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

def inbounds(i, j, m):
        return i >= 0 and i < len(m) and j >= 0 and j < len(m[i])

def runsim(m, gi, gj, dir):
        F = True
        vp2 = set()
        vp1 = set()

        while inbounds(gi, gj, m):
            if m[gi][gj] == '#':
                gi, gj = gi - dirs[dir][0], gj - dirs[dir][1]
                dir = (dir + 1) % 4
                continue
        
            if (gi, gj, dir) in vp2:
                F = False
                break
            
            vp2.add((gi, gj, dir))
            vp1.add((gi, gj))

            gi, gj = gi + dirs[dir][0], gj + dirs[dir][1]

        return vp1, vp2, F

def part1():
    m = []

    for line in lines:
        m.append(list(line))

    gi, gj = 0, 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == "^":
                gi, gj = i, j
                break

    vp1, _, _ = runsim(m, gi, gj, 0)

    print(len(vp1))
    

def part2():
    m = []
    c = 0

    for line in lines:
        m.append(list(line))

    si, sj = 0, 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == "^": si, sj = i, j
    
    vp1, _, _ = runsim(m, si, sj, 0)

    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == "#": continue
            if (i, j) not in vp1: continue

            if i != si or j != sj:
                m[i][j] = "#"
                if not runsim(m, si, sj, 0)[2]:
                    c += 1
                m[i][j] = "."
    print(c)

# part1()

part2()
