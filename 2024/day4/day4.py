lines = open('/Users/architwankhade/Downloads/AdventOfCode/2024/day4/input.txt').read().splitlines()

def inbound(i, j, ws):
    return i >= 0 and i < len(ws) and j >= 0 and j < len(ws[i])

def check_diag(i, j, ws):
    c = 0

    if inbound(i-3, j-3, ws) and ws[i-3][j-3] == "S":
        if ws[i-1][j-1] == "M" and ws[i-2][j-2] == "A":
            c += 1
    
    if inbound(i+3, j+3, ws) and ws[i+3][j+3] == "S":
        if ws[i+1][j+1] == "M" and ws[i+2][j+2] == "A":
            c += 1
    
    if inbound(i-3, j+3, ws) and ws[i-3][j+3] == "S":
        if ws[i-1][j+1] == "M" and ws[i-2][j+2] == "A":
            c += 1
    
    if inbound(i+3, j-3, ws) and ws[i+3][j-3] == "S":
        if ws[i+1][j-1] == "M" and ws[i+2][j-2] == "A":
            c += 1
    
    return c

def part1():
    ws = []
    c = 0
    for line in lines:
        c += line.count("XMAS")
        c += line.count("SAMX")
        ws.append(list(line))
    
    for i in range(len(ws)):
        for j in range(len(ws[i])):
            if ws[i][j] == "X":
                c += check_diag(i, j, ws)

    ws = list(zip(*ws[::-1]))


    for i in range(len(ws)):
        nl = "".join(ws[i])
        c += nl.count("XMAS")
        c += nl.count("SAMX")

    print(c)

part1()

def check_diag2(i, j, ws):
    if inbound(i-1, j-1, ws) and inbound(i+1, j+1, ws) and inbound(i-1, j+1, ws) and inbound(i+1, j-1, ws):
        if ws[i-1][j+1] == ws[i+1][j+1] and ws[i-1][j-1] == ws[i+1][j-1] and ws[i-1][j+1] != ws[i-1][j-1]:
            if (ws[i-1][j-1] == "M" and ws[i+1][j+1] == "S") or (ws[i-1][j-1] == "S" and ws[i+1][j+1] == "M"): return 1
            
        if ws[i-1][j+1] == ws[i-1][j-1] and ws[i+1][j-1] == ws[i+1][j+1] and ws[i+1][j+1] != ws[i-1][j-1]:
            if (ws[i-1][j-1] == "M" and ws[i+1][j+1] == "S") or (ws[i-1][j-1] == "S" and ws[i+1][j+1] == "M"): return 1
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