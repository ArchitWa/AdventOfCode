lines = open('/Users/architwankhade/Downloads/AdventOfCode/2024/day7/input.txt').read().splitlines()

def recurse(prod, temp, nums):
    if temp > prod:
        return False;
    if len(nums) == 0:
        return prod == temp
    
    
    return recurse(prod, temp + nums[0], nums[1:]) or recurse(prod, (1 if temp == 0 else temp) * nums[0], nums[1:]) or recurse(prod, int(str(temp) + str(nums[0])), nums[1:])

def part1and2():
    c = 0
    for line in lines:
        prod, nums = line.split(":")
        prod = int(prod)
        nums = list(map(int, nums.strip().split(" ")))
        
        if recurse(prod, 0, nums):
            c += prod

    print(c)
        

part1and2()