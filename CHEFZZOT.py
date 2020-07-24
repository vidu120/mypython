N = int(input())
i = 0
b = 0
mine = True
maxLength = 0
for x in input().split():
    x = int(x)
    if x == 0:
        if mine:
            a = i
            maxLength = max(maxLength , a - b)
            b = i
            mine = False
        else:
            a = i
            maxLength = max(maxLength , a - b - 1)
            b = i
    i = i + 1
if not mine:
    maxLength = max(maxLength , N - 1 - b)
else:
    maxLength = N
print(maxLength)