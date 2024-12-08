lines = open('/Users/architwankhade/Downloads/AdventOfCode/2024/day8/input.txt').read().splitlines()

def solve(p2):
    nodes = {}
    antinodes = set()
    map = [list(line) for line in lines]

    for i, row in enumerate(map):
        for j, val in enumerate(row):
            if val != ".":
                nodes.setdefault(val, []).append((i, j))
            
    def distance(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    def inline(an, n1, n2):
        return (n2[1] - an[1]) * (n1[0] - an[0]) == (n1[1] - an[1]) * (n2[0] - an[0])
    
    def inbw(an, n1, n2):
        return (min(n1[0], n2[0]) <= an[0] <= max(n1[0], n2[0]) and
                min(n1[1], n2[1]) <= an[1] <= max(n1[1], n2[1]))

    for i in range(len(map)):
        for j in range(len(map[i])):
            for node in nodes:
                if len(nodes[node]) == 1: continue
                for k in range(len(nodes[node])):
                    for l in range(len(nodes[node])):
                        if k == l or (i, j) in antinodes or inbw((i,j), nodes[node][k], nodes[node][l]): continue
                            
                        if p2: antinodes.update([nodes[node][k], nodes[node][l]])

                        if not inline((i, j), nodes[node][k], nodes[node][l]): continue

                        if not p2 and distance((i, j), nodes[node][k]) * 2 != distance((i, j), nodes[node][l]):  continue
                        
                        antinodes.add((i, j))
                    
    if p2: [antinodes.add(n) for node in nodes if len(nodes[node]) > 1 for n in nodes[node]]
    
    print(len(antinodes))

solve(p2=False)
solve(p2=True)

                        

                    