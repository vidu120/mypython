N, D = map(int, input().split())
L = []
if N == 1:
    print('0')
    exit
for i in range(N):
    L.append(int(input()))
L.sort()
ans = 0
for i in range(1 ,N):
    if L[i] - L[i-1] <= D:
        ans = ans + 1
        i = i + 2
print(ans)