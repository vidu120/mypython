N1, N2, N3 = [int(x) for x in input().split()]
L = []
for i in range(N1 + N2 + N3):
    L.append(int(input()))
L.sort()
ans=0
final=[]
elem=L[0]
hm=False
for i in range(1, len(L)):
    if L[i] == elem and hm==False:
        ans=ans + 1
        final.append(L[i])
        hm=True
    else:
        elem=L[i]
        hm=False
print(ans)
for i in final:
    print(i)
