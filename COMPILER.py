T = int(input())
for _ in range(T):
    s = input()
    if len(s) == 1:
        print(0)
        continue
    ans = 0
    ty = 0
    tm = 0
    for i in range(len(s)):
        if s[i] == '<':
            ans = ans + 1
            ty = i
        elif s[i] == '>':
            ans = ans - 1
            if ans < 0:
                if i == 0:
                    ans = -1
                else:
                    ans = ty
                break
            elif ans == 0:
                tm = i
            ty = i
    else:
        if tm == 0:
            tm = -1
        ans = tm
    print(ans + 1)