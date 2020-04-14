t = int(input())


def marryme(a, b):
    x = 0
    for i in range(len(b)):
        if b[i] == a[x]:
            x = x + 1
        if x == len(a):
            return 1
    return 0


while t > 0:
    N, M = map(str, input().split())
    if len(N) <= len(M):
        if marryme(N, M):
            print('YES')
        else:
            print('NO')
    else:
        if marryme(M, N):
            print('YES')
        else:
            print('NO')
    t = t - 1
