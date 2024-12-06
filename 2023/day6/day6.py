lines = open('/Users/architwankhade/Downloads/AdventOfCode/day6/input.txt').read().split("\n")

def part1():
    t = [int(x) for x in lines[0].split(': ')[1].split(' ') if x != '']
    d = [int(x) for x in lines[1].split(': ')[1].split(' ') if x != '']
    s = 1

    for i, time in enumerate(t):
        c = 0
        for j in range(0, time+1):
            if abs(time - j) * j > d[i]: c += 1
        s *= c
    print(s)


def part2():
    t = int(lines[0].split(': ')[1].replace(' ', ""))
    d = int(lines[1].split(': ')[1].replace(' ', ""))

    c = 0
    for j in range(0, t+1):
        if abs(t - j) * j > d: c += 1

    print(c)
part2()