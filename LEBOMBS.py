t = int(input())
while t > 0:
    N = int(input())
    S = input()
    final = [0 for x in range(N)]
    if N == 1:
        if S[0] == '0':
            print(1)
        else:
            print(0)
        continue
    for i in range(N):
        if i == 0:
            if S[i] == '1':
                final[i], final[i+1] = 1, 1
        elif i == N - 1:
            if S[i] == '1':
                final[i] = 1
                final[i - 1] = 1
        else:
            if S[i] == '1':
                final[i-1] = 1
                final[i] = 1
                final[i+1] = 1
    print(final.count(0))
    t = t - 1
