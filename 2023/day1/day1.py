lines = open('/Users/architwankhade/Downloads/AdventOfCode/day1/input.txt').read().splitlines()

# Part 1
def part1():
    n = "1234567890"
    s = 0
    for i in range(len(lines)):
        a = [x for x in lines[i] if x in n]
        s += int(a[0] + "" +  a[-1])

    return s

# Part 2
def part2():
    n, s = "1234567890", 0
    for i in range(len(lines)):
        l = lines[i].replace("one", "one1one").replace("two", "two2two").replace("three", "three3three").replace("four", "four4four").replace("five", "five5five").replace("six", "six6six").replace("seven", "seven7seven").replace("eight", "eight8eight").replace("nine", "nine9nine").replace("zero", "zero0zero")
        a = [x for x  in l if x in n]
        s += int(a[0] + "" +  a[-1])

    return s

print(part2())