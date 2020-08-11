T = int(input())
while T > 0:
    N = int(input())
    arr = [int(x) for x in input().split()]
    print(arr.index(min(arr)) + 1)
    T = T - 1   