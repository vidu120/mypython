T = int(input())
while T > 0:
    N = int(input())
    L = [int(x) for x in input().split()]
    L = set(L)
    print(len(L))
    T = T - 1
