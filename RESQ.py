import math
T  = int(input())
while T > 0:
    N = int(input())
    a = math.isqrt(N)
    while True:
        if N % a == 0:
            print(abs((N//a) - a))
            break
        a = a - 1
    T = T - 1