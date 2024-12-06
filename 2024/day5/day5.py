from functools import cmp_to_key
lines = open('/Users/architwankhade/Downloads/AdventOfCode/2024/day5/input.txt').read().splitlines()

notpassed = []

def part1():
    r = {}
    s = 0
    for line in lines:
        if "|" in line:
            a, b = line.split("|")
            if a in r: r[a].append(int(b))
            else: r[a] = [int(b)]
            continue
        
        if line == "": continue

        rules = list(map(int, line.split(",")))
        F = True

        for i in range(len(rules)-1):
            remaining = rules[i+1:]
            for j in range(len(remaining)):
                if str(rules[i]) not in r.keys() or remaining[j] not in r[str(rules[i])] : 
                    F = False
                    break

        if F: s += rules[int(len(rules)/2)]
        else: notpassed.append(rules) 
    
    print(s)

part1()

def part2():
    r = {}
    s = 0
    for line in lines:
        if "|" in line:
            a, b = line.split("|")
            if b in r:
                r[b].append(int(a))
            else:
                r[b] = [int(a)]
            continue
        
    def compare(a, b):
        if a in r[str(b)]:
            return -1
        if b in r[str(a)]:
            return 1
        return 0

    for np in notpassed:
        np = sorted(np, key=cmp_to_key(compare))
        s += np[int(len(np)//2)]
    
    print(s)

part2()
    
# 4944