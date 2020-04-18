T = int(input())
for _  in range(T):
    K = int(input())
    L = []
    for i in range(K//25):
        for j in range(26):
            L.append(j+97)
    if K % 25 > 0:
        L.append(97)
    for i in range(K%25):
        L.append(i + 98)
    for i in range(len(L)-1,-1,-1):
        print(chr(L[i]),end = '')
    print()
