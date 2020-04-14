from math import sqrt
t = int(input())


def isprime(a=1):
    for i in range(2, int(sqrt(a)) + 1):
        if a % i == 0:
            return 0
    return 1


def winning_streak(N):
    global ans
    for i in range(N - 1, 0, -1):
        if isprime(i) == 1:
            N = N - i
            ans = not(ans)
            return winning_streak(N)
    return ans


while t > 0:
    MINE = int(input())
    ans = True
    if winning_streak(MINE) == False:
        print('BOB')
    else:
        print('ALICE')
    t = t - 1
