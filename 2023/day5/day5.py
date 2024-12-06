lines = open('/Users/architwankhade/Downloads/AdventOfCode/day5/input.txt').read().split("\n\n")
import sys

def part1():
    inp = list(map(int, lines[0].split(': ')[1].strip().split(' ')))


    for c in [1,2,3,4,5,6, 7]:
        for i,seed in enumerate(inp):
            for line in lines[c].splitlines()[1:]:
                dest, src, r = list(map(int, line.split(" ")))
                if src <= seed < src + r:
                    inp[i] = seed - src + dest    
    print(min(inp))

def part2():
    oi = list(map(int, lines[0].split(': ')[1].strip().split(' ')))
    inp = []
    min = sys.maxsize
    start = 0

    while start < len(oi):
        seed = oi[start]
        while seed < oi[start] + oi[start+1]:
            curr, seed= seed, -1
            for c in [1,2,3,4,5,6, 7]:
                for line in lines[c].splitlines()[1:]:
                    dest, src, r = map(int, line.split(" "))
                    if src <= curr and (curr - src) < r:
                        if seed == -1: seed += src + r
                        curr -= src + r
                        break
            if curr < min: min = curr
        start +=2


    print(min)

part2()