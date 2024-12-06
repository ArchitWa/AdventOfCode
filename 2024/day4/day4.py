lines = open('/Users/architwankhade/Downloads/AdventOfCode/2024/day4/input.txt').read().splitlines()

def inbound(i, j, ws):
    return i >= 0 and i < len(ws) and j >= 0 and j < len(ws[i])

def check_diag(i, j, ws):
    c = 0

    for x in [-1 , 1]:
        for y in [-1, 1]:
            if inbound(i+3*x, j+3*y, ws) and ws[i+3*x][j+3*y] == "S":
                if ws[i+x][j+y] == "M" and ws[i+2*x][j+2*y] == "A":
                    c += 1

    return c

def part1():
    ws = []
    c = 0

    for line in lines:
        ws.append(list(line))
    rws = list(zip(*ws[::-1]))
    
    for i in range(len(ws)):
        for j in range(len(ws[i])):
            if ws[i][j] == "X":
                c += check_diag(i, j, ws)

    for i in range(len(ws)):
        l, nl = "".join(ws[i]), "".join(rws[i])
        c += nl.count("XMAS") + nl.count("SAMX") + l.count("XMAS") + l.count("SAMX")

    print(c)

part1()

def check_diag2(i, j, ws):
    l = {"X" : 0, "M" : 0, "A": 0, "S": 0}

    for x in [-1, 1]:
        for y in [-1, 1]:
            if inbound(i+x, j+y, ws):
                l[ws[i+x][j+y]] += 1

    if l["M"] == l["S"] == 2 and ws[i-1][j-1] != ws[i+1][j+1]: return 1
    return 0
    
def part2():
    ws = []
    c = 0

    for line in lines:
        ws.append(list(line))
    
    for i in range(len(ws)):
        for j in range(len(ws[i])):
            if ws[i][j] == "A":
                c += check_diag2(i, j, ws)
    
    print(c)

part2()    