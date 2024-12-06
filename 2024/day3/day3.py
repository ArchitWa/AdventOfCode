lines = open('/Users/architwankhade/Downloads/AdventOfCode/2024/day3/input.txt').read().splitlines()

def part1():
    s = 0
    for line in lines:
        a = line.split("mul")

        for exp in a:
            if exp[0] == "(" and ")" in exp:
                exp = exp[1:exp.index(")")]
                if "," in exp:
                    exp = exp.split(",")
                    if exp[0].strip() == exp[0] and exp[1].strip() == exp[1] and exp[0].isnumeric() and exp[1].isnumeric():
                        s += int(exp[0]) * int(exp[1])
                else: continue
                
            else: continue
    print(s)

part1()

def checkEnabled(exp, enabled):
    if "don't()" in exp:
        return False
    if "do()" in exp:
        return True
    return enabled
    

def part2():
    s = 0
    enabled = True
    for line in lines:
        a = line.split("mul")
        for exp in a:
            t = exp
            if exp[0] == "(" and ")" in exp:
                exp = exp[1:exp.index(")")]
                if "," in exp:
                    exp = exp.split(",")
                    if exp[0].strip() == exp[0] and exp[1].strip() == exp[1] and exp[0].isnumeric() and exp[1].isnumeric():
                        if enabled: s += int(exp[0]) * int(exp[1])
                    enabled = checkEnabled(t, enabled)
                else: 
                    enabled = checkEnabled(t, enabled)
                    continue
            else: 
                enabled = checkEnabled(t, enabled)
                continue
    
    print(s)

part2()
