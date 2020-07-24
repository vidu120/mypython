T = int(input())

def GCD(x , y):
    if y == 0:
        return x
    return GCD(y , x % y)

while T > 0:
    N = int(input())
    elements = [int(x) for x in input().split()]
    GCDelem = 0
    for elem in elements:
        GCDelem = GCD(GCDelem , elem)
    if GCDelem == 1:
        print(N)
    else:
        print(-1)
    T = T - 1