lines = open('/Users/architwankhade/Downloads/AdventOfCode/2024/day9/input.txt').read().splitlines()

def part1():
    inp = list(map(int, lines[0]))
    fd = []

    def divided(inp):
        _, end = inp[0:inp.index(".")], inp[inp.index(".") + 1:]
        if "." in end:
            if ["."] * len(end) == end:
                return True
            
        return False
    
    for i in range(len(inp)):
        if i % 2 == 0:
            fd.append([i//2] * inp[i])
        else:
            if inp[i] == 0: continue
            fd.append(inp[i] * ["."])
    
    fd = [item for sublist in fd for item in sublist]

    idx = len(fd) - 1

    while not divided(fd):
        if fd[idx] == ".":
            idx -= 1
            continue
        
        val = fd[idx]
        fd[idx] = "."
        fd[fd.index(".")] = val
        idx -= 1

    n = 0
    for i in range(len(list(fd))):
        if fd[i] == ".":
            continue
        n += int(fd[i]) * i

    print(n)

# part1()

def part2():
    inp = list(map(int, lines[0]))
    
    d = [["." if i % 2 else i // 2, int(num)] for i, num in enumerate(inp) if int(num) > 0]
    idx = 1

    while idx < len(d):
        if d[-idx][0] == ".": 
            idx += 1
            continue

        for freei in range(len(d) - idx):
            if d[freei][0] == ".":
                if d[freei][1] == d[-idx][1]:
                    d[freei][0] = d[-idx][0]
                elif d[freei][1] > d[-idx][1]:
                    d[freei][1] -= d[-idx][1]
                    d.insert(freei, [d[-idx][0], d[-idx][1]])
                else:
                    continue
                d[-idx][0] = "."
                break
        
        idx += 1

    s, curr = 0, -1
    for i in range(len(d)):
        for _ in range(d[i][1]):
            curr += 1
            if d[i][0] == ".": continue
            s += d[i][0] * curr

    print(s)

part2()
