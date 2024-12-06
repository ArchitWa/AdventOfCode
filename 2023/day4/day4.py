lines = open('/Users/architwankhade/Downloads/AdventOfCode/day4/input.txt').read().splitlines()

def part1():
    s = 0
    for line in lines: 
        cards = line.split(": ")
        winning = [int(i) for i in cards[1].split("|")[0].strip().split(" ") if i.isdigit()]
        hand = [int(i) for i in cards[1].split("|")[1].strip().split(" ") if i.isdigit()]

        n = sum([1 for i in hand if i in winning])
        if n!=0: s += (2**(n-1))
    print(s)

def part2():
    c = []
    for line in lines: 
        cards = line.split(": ")
        c.append([
                [int(i) for i in cards[1].split("|")[0].strip().split(" ") if i.isdigit()], # winning
                [int(i) for i in cards[1].split("|")[1].strip().split(" ") if i.isdigit()] # hand
        ])

    co = [1 for _ in range(len(c))]

    for i,_c in enumerate(c):
        n = sum([1 for i in _c[1] if i in _c[0]])
        for j in range(n):
            co[i+j+1] += co[i]


    print(sum(co))
part2()
