#!/usr/bin/env python3

import numpy as np
T = int(input())
while T > 0:
    N = int(input())
    arr = [int(x) for x in input().split()]
    resultArray = abs(np.array(arr[:N - 1]) - np.array(arr[1:])) - 1
    print(resultArray.sum(axis = 0))
    T = T - 1
