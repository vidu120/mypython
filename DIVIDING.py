N = int(input())
ans = 0
for x in input().split():
    ans = ans + int(x)
if ans == (N * (N + 1))//2:
    print('YES')
else:
    print('NO')