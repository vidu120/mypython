T = int(input())
while T > 0:
    N = int(input())
    stoneInPiles = [int(x) for x in input().split()]
    stoneInPiles.sort(reverse = True)
    ans = 0
    for i in range(0 , N , 2):
        ans += stoneInPiles[i]
    print(ans)
    T = T - 1