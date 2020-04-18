T = int(input())
for _ in range(T):
    L, D, S, C = map(int, input().split())
    for _ in range(D):
        if S >= L:
            print('ALIVE AND KICKING')
            break
        S = S * (C+1)
    else:
        print('DEAD AND ROTTING')
