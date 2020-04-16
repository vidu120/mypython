T = int(input())
while T > 0:
    N = int(input())
    if N > 360:
        print('n n n')
    else:
        if 360 % N == 0:
            print('y',end = ' ')
        else:
            print('n', end = ' ')
        print('y',end = ' ')
        if N <= 26:
            print('y')
        else:
            print('n') 
    T = T - 1
