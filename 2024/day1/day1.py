lines = open('/Users/architwankhade/Downloads/AdventOfCode/2024/day1/input.txt').read().splitlines()


def part1():
    le, ri = [], []
    for line in lines:
        le.append(int(line.split("   ")[0]))
        ri.append(int(line.split("   ")[1]))
    le, ri = list(map(int, sorted(le))), list(map(int, sorted(ri)))

    d = [abs(le[i] - ri[i]) for i in range(len(le))]
    print(sum(d))

part1()

def part2():
    le, ri = [], []
    for l in lines:
        le.append(int(l.split("   ")[0]))
        ri.append(int(l.split("   ")[1]))
    
    s = [le[i] * ri.count(le[i]) for i in range(len(le))]
    print(sum(s))

part2()