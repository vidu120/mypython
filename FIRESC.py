T = int(input())
while T > 0:
    N , M = map(int ,input().split())
    friendList = []
    stacks = []
    for i in range(M):
        friendList.append([int(x) for x in input().split()])
    stacks = [friendList[0]]
    mine = [False for _ in range(N)]
    mine[friendList[0][1] - 1] = True
    mine[friendList[0][0] - 1] = True
    for i in range(M):
        for friendPair in stacks:
            if (friendList[i][0] in friendPair) and (friendList[i][1] in friendPair):
                break
            elif friendList[i][1] in friendPair:
                friendPair.append(friendList[i][0])
                mine[friendList[i][0] - 1] = True
                break
            elif friendList[i][0] in friendPair:
                friendPair.append(friendList[i][1])
                mine[friendList[i][1] - 1] = True
                break
        else:
            stacks.append(friendList[i])
            mine[friendList[i][0] - 1] = True
            mine[friendList[i][1] - 1] = True
    for i in range(N):
        if not mine[i]:
            stacks.append([i + 1])
    noOfFireEscapes = len(stacks) % 1000000007
    selectingCaptain = 1
    for stack in stacks:
        selectingCaptain = (selectingCaptain * len(stack)) % 1000000007
    print(noOfFireEscapes , selectingCaptain)
    T = T - 1