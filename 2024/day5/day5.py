from functools import cmp_to_key
lines = open('/Users/architwankhade/Downloads/AdventOfCode/2024/day5/input.txt').read()

r = {}
lines = lines.split("\n\n")
RULES = [list(map(int, line.split(","))) for line in lines[1].splitlines()]

def compare(a, b):
    if a in r[str(b)]:
        return -1
    if b in r[str(a)]:
        return 1
    return 0

for line in lines[0].splitlines():
    a, b = line.split("|")
    if b in r:
        r[b].append(int(a))
    else:
        r[b] = [int(a)]

def part1():
    passed = [rule for rule in RULES if rule == sorted(rule, key=cmp_to_key(compare))]
    print(sum([rule[int(len(rule)/2)] for rule in passed]))

    return [rule for rule in RULES if rule not in passed]
    

def part2(notpassed):
    print(sum([np[int(len(np)//2)] for np in [sorted(np, key=cmp_to_key(compare)) for np in notpassed]]))

part2(part1())
    
# 4944