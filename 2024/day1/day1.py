lines = open('/Users/architwankhade/Downloads/AdventOfCode/2024/day1/input.txt').read().splitlines()


def part1():
    le, ri = [], []
    for line in lines:
        le.append(int(line.split("   ")[0]))
        ri.append(int(line.split("   ")[1]))
    le = sorted(le)
    ri = sorted(ri)

    d = 0
    for i in range(len(le)):
        d += abs(int(le[i]) - int(ri[i]))
    print(d)

part1()

def part2():
    le, ri = [], []
    for l in lines:
        le.append(int(l.split("   ")[0]))
        ri.append(int(l.split("   ")[1]))
    
    s = 0
    for i in range(len(le)):
        s += le[i] * ri.count(le[i])
    print(s)

part2()