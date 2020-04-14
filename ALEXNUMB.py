T = int(input())
while T > 0:
    N = int(input())
    L = [int(x) for x in input().split()]
    if N == 1:
        print(0)
        T = T - 1
        continue
    ans = (N * (N-1))//2
    L.sort()
    a = 1
    for i in range(1,N):
        if L[i] == L[i-1]:
            a = a + 1
        else :
            ans -= (a * (a-1))//2
            a = 1
    print(ans)
    T = T - 1
