n = int(input())


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


while n > 0:
    A, B = map(int, input().split())
    print(gcd(A, B))
    n = n - 1
