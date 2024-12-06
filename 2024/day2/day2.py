lines = open('/Users/architwankhade/Downloads/AdventOfCode/2024/day2/input.txt').read().splitlines()

def check(a):
    inc = dec = True

    for i in range(len(a) - 1):
        if abs(a[i] - a[i + 1]) < 1 or abs(a[i] - a[i + 1]) > 3: return False
        
        if a[i] - a[i + 1] < 0: dec = False
        else: inc = False
            
    return inc or dec

def part1():
    r = 0
    for l in lines:
        a = list(map(int, l.split(" ")))
        if check(a): r += 1
    print(r)

part1()

def part2():
    r = 0
    for l in lines:
        a = list(map(int, l.split(" ")))
        
        if check(a): r += 1
        else:
            for i in range(len(a)):
                m = a[0:i] + a[i+1:]
                if check(m):
                    r += 1
                    break
    print(r)

part2()
