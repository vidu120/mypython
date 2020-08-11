T = int(input())
while T > 0:
    S = input()
    maxJump = 1
    pr = 0
    daysToCross = 0
    for char in S:
        if char == '.':
            pr = pr + 1
        elif pr + 1 > maxJump:
            maxJump = pr + 1
            daysToCross = daysToCross + 1
            pr = 0
        else:
            pr = 0
    print(daysToCross)
    T = T - 1