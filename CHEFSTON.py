import numpy as np

T = int(input())

while T > 0:
    N, K = map(int, input().split())

    arr = np.array([K // int(x) for x in input().split()])

    arr0 = np.array([int(x) for x in input().split()])

    result = arr * arr0

    print(np.max(result))    
    
    T = T - 1
