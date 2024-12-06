lines = open('/Users/architwankhade/Downloads/AdventOfCode/day3/input.txt').read().splitlines()



def inBound(t, r, c):
    return r >= 0 and r < len(t) and c >= 0 and c < len(t[r])

# Part 1
def part1():
    s = found = 0
    t = []
    for line in lines: t.append(list(line))

    def check_neighbors(t, r, c, l):
        for i in range(-1, 2):
            for j in range(-1, l+1):
                if inBound(t, r+i, c+j) and (t[r+i][c+j]) not in "0123456789." :
                    return True
        return False

    for r in range(len(t)):
        for c in range(len(t[r])):
            if found > 0:
                found -= 1
                continue
            
            if t[r][c].isdigit():
                l = 0
                for i in range(3):
                    if c+i < len(t[r]) and t[r][c+i].isdigit(): l += 1
                    else: break

                if check_neighbors(t, r, c, l):                  
                    s += int("".join(t[r][c:c+l]))
                    found = l
                    
    print(s)


# Part 2
def part2():
    s = 0
    t = []
    for line in lines: t.append(list(line))
    
    def extractNum(t, r, c):
        line = t[r]
        p = line[c]
        if not line[c+1].isdigit():
            if c-1 >= 0 and line[c-1].isdigit():
                p = line[c-1] + p
                if c-2 >= 0 and line[c-2].isdigit():
                    p = line[c-2] + p
        elif not line[c-1].isdigit():
            if c+1 < len(line) and line[c+1].isdigit():
                p += line[c+1]
                if c+2 < len(line) and line[c+2].isdigit():
                    p += line[c+2]
        else:
            p = line[r][c-1:c+2]
        return p
      

    def check_gears(t, r, c):
        n = [t[r-1][c-3:c+4], t[r][c-3:c+4], t[r+1][c-3:c+4]]
        r, c = 1, 3
        a = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                if inBound(n, r+i, c+j):
                    if n[r+i][c+j].isdigit():
                        a.append(extractNum(n, r+i, c+j))
              
        b = [int(x) for x in a if x.isdigit()]
        c = []

        for i in b:
            if i not in c:
                c.append(i)

        return [c[0], c[1]] if len(c) >= 2 else [0, 0]

    for r in range(len(t)):
        for c in range(len(t[r])):
            if t[r][c] == "*":
                a, b = check_gears(t, r, c)
                s += a * b
    
    print(s)
    
    
                

part2()