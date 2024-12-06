from functools import cmp_to_key

lines = open('/Users/architwankhade/Downloads/AdventOfCode/day7/input.txt').read().split("\n")
k = "AKQT98765432J"


def compare_cards(card1, card2):
    card1, card2 = card1[0], card2[0]
    
    s1, s2 = get_score(card1), get_score(card2)
    if s1 < s2: return 1
    elif s1 > s2: return -1
    else:
        i = 0
        while i < 5:
            if k.index(card1[i]) > k.index(card2[i]): return -1
            elif k.index(card1[i]) < k.index(card2[i]): return 1
            else: i += 1

def get_score(card):
    c = {i:card.count(i) for i in k}

    m = max(c.items(), key=lambda k: k[1])[0]
    if m[0] != "J":
        c[m[0]] += c["J"]  
    else:
        d = {i:card.count(i) for i in k}
        d["J"] = 0
        n = max(d.items(), key=lambda k: k[1])[0]
        c[n] += c["J"]
    c["J"] = 0

    if 5 in c.values(): return 1
    elif 4 in c.values(): return 2
    elif 3 in c.values() and 2 in c.values(): return 3
    elif 3 in c.values() and 1 in c.values(): return 4
    elif "".join(list(map(str, c.values()))).count("2") == 2: return 5
    elif 2 in c.values(): return 6
    else: return 7


def part1():
    cards = []
    for line in lines:
        c, pts = line.split()
        cards.append([c, int(pts)])
  
    cards = sorted(cards, key=cmp_to_key(compare_cards))
    s = sum([(i+1)*card[1] for i,card in enumerate(cards)])

    print(s)

def part2():
    cards = []
    for line in lines:
        c, pts = line.split()
        cards.append([c, int(pts)])
    
    cards = sorted(cards, key=cmp_to_key(compare_cards))
    s = sum([(i+1)*card[1] for i,card in enumerate(cards)])

    print(s)

part2()

