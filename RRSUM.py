N, M = map(int, input().split())
min = N + 2
max = 3 * N
while M > 0:
    q = int(input())
    if q < min or q > max:
        print(0)
    else:
        if q + 1 -min <= N:
            print(q + 1 - min)
        else:
            print(max - q + 1)
    M = M - 1
