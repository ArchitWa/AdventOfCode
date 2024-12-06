lines = open('/Users/architwankhade/Downloads/AdventOfCode/day2/input.txt').read().splitlines()

# Part 1
def part1():
    s = 0
    for line in lines:
        m = {"red": 12, "green": 13, "blue": 14}
        flag = False
        l = line.split(":")
        id = int(l[0].split(" ")[1])

        for di in l[1].replace(";", ",").split(","):
            n = di.strip().split(" ")
            if int(n[0].strip()) > m[n[1].strip()]: flag = True

        if flag == False: s += id
    
    print(s)

part1()

# Part 2
def part2():
    s = 0
    for line in lines:
        m = [0,0,0]
        f = {"red": 0, "green": 1, "blue": 2}
        for di in line.split(":")[1].split(";"):
            for i in di.split(", "):
                n = i.strip().split(" ")
                if int(n[0].strip()) > m[f[n[1].strip()]]:
                    m[f[n[1].strip()]] = int(n[0].strip())
               

        s += m[0] * m[1] * m[2]
    
    print(s)

part2()