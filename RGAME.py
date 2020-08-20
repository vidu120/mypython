#!/usr/bin/env python3
T = int(input())
div = 10**9 + 7
for _ in range(T):
    n = int(input())
    A = [int(x) for x in input().split()]
    score = 0
    p = 1
    c = A[0]
    for i in range(1, n+1):
        score = (2*score + 2*A[i]*c) % div
        c = (c + p*A[i]) % div
        p = (p*2) % div
    print(score)