T = int(input())
for _ in range(T):
    L, R = map(int, input().split())
    ans = 0
    if L % 10 != 0:
        if L % 10 <= 2:
            pass
        elif L % 10 <= 3:
            ans -= 1
        elif L % 10 <= 9:
            ans -= 2
    L = L - (L % 10)

    if R % 10 != 0:
        if R % 10 < 2:
            pass
        elif R % 10 < 3:
            ans = ans + 1
        elif R % 10 < 9:
            ans = ans + 2
        else:
            ans = ans + 3
    R = R - (R % 10)

    ans += ((R - L)//10)*3

    print(ans)
