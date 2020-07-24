T = int(input())
for _ in range(T):
    N, C, Q = map(int, input().split())
    for _ in range(Q):
        L, R = map(int, input().split())
        if C >= L and C <= R:
            C = R - C + L
    print(C)
