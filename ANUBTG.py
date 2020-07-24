T = int(input())
while T > 0:
    N = int(input())
    items = [int(x) for x in input().split()]
    items.sort(reverse = True)
    count = 0
    for i in range(0 , N , 4):
        if i + 1 < N:
            count += items[i] + items[i + 1]
        else:
            count += items[i]
    print(count)
    T = T - 1