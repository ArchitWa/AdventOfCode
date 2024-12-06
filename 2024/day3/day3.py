lines = open('/Users/architwankhade/Downloads/AdventOfCode/2024/day3/input.txt').read().splitlines()

def part1():
    s = 0
    for line in lines:
        muls = line.split("mul")

        for exp in muls:
            if exp[0] == "(" and ")" in exp:
                exp = exp[1:exp.index(")")]
                if "," in exp:
                    exp = exp.split(",")
                    if exp[0].strip() == exp[0] and exp[1].strip() == exp[1] and exp[0].isnumeric() and exp[1].isnumeric():
                        s += int(exp[0]) * int(exp[1])
    print(s)

part1()

def checkEnabled(exp, enabled):
    return False if "don't()" in exp else True if "do()" in exp else enabled
    

def part2():
    s = 0
    enabled = True
    for line in lines:
        muls = line.split("mul")
        for exp in muls:
            t = exp
            if exp[0] == "(" and ")" in exp:
                exp = exp[1:exp.index(")")]
                if "," in exp:
                    exp = exp.split(",")
                    if enabled: 
                        if exp[0].strip() == exp[0] and exp[1].strip() == exp[1] and exp[0].isnumeric() and exp[1].isnumeric():
                            s += int(exp[0]) * int(exp[1])

            enabled = checkEnabled(t, enabled)
    
    print(s)

part2()
