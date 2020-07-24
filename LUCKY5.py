T = int(input())
for _ in range(T):
    N = input()
    print(N)
    ans = 0
    for i in range(len(N)):
        if N[i] != "4" and N[i] != "7":
            ans = ans + 1
    print(ans)