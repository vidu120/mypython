import math
t = int(input())
while t > 0:
    P, S = [int(x) for x in input().split()]
    a = (P/2 + math.sqrt((P**2) - (24*S)))/6
    b = (P/4 - a)/2
    print(f'{a*b*b:0.2f}')
    t = t - 1
