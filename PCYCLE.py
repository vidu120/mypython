N = int(input())
L = [int(x) for x in input().split()]
need = [True for x in range(N)]
ans = 0
finalised = [[] for x in range(N) ]
x = 0
j = 0
for i in range(N):
    if need[i]:
        finalised[ans].append(i + 1)
        j = i
        while True:
            finalised[ans].append(L[j])
            need[j] = False
            j = L[j] - 1
            if j == i:
                ans = ans + 1
                break
print(ans)
for i in range(ans):
    for j in range(len(finalised[i])):
        print(finalised[i][j] , end = ' ')
    print()