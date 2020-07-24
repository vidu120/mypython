T = int(input())
while T > 0:
    S = input()
    total = 0
    for character in S:
        if character >= (chr)(48) and character <= (chr)(57):
            total += (int)(character)
    print(total)
    T = T - 1