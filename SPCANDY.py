T = int(input())
while T > 0:
    N , K = [int(x) for x in input().split()]
    print(N // K , N % K )
    T = T - 1