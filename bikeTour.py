T = int(input())
for j in range(T):
    N = int(input())
    H = [int(x) for x in input().split()]
    ans = 0
    for i in range(1,N-1):
        if H[i] > H[i-1] and H[i] > H[i+1]:
            ans = ans + 1
    print(f'Case #{j+1}: {ans}')