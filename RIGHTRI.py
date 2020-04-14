N = int(input())
ans = 0
for i in range(N):
    x1, y1, x2, y2, x3, y3 = [int(x) for x in input().split()]
    if (y2 - y1)*(y3-y1) + (x2-x1)*(x3-x1) == 0 or (y2-y1)*(y3-y2) + (x2-x1)*(x3-x2) == 0 or (y2-y3)*(y3-y1) + (x2-x3)*(x3-x1) == 0:
        ans = ans + 1
print(ans)
