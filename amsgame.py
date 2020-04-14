t = int(input())


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


while t > 0:
    n = int(input())
    L = [int(x) for x in input().split()]
    mine = L[0]
    for x in L[1:]:
        mine = gcd(max(x, mine), min(x, mine))
    print(mine)
    t = t - 1
