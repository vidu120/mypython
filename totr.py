T, M = [x for x in input().split()]
L = {'_': ' ', '?': '?', '.': '.', ',': ',', '!': '!'}
for i in range(26):
    L[chr(i + 97)] = M[i]
T = int(T)
while T > 0:
    sen = input()
    for i in sen:
        if i.isupper():
            print(L[i.lower()].upper(),end = '')
        else:
            print(L[i], end='')
    print()
    T = T - 1