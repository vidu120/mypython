T = int(input())
while T > 0:
	N = int(input())
	L = [int(x) for x in input().split()]
	for i in range(N):
		if L[i] == i or L[i] == i + 1 or L[i] == i + 2:
			continue
		else:
			print("NO")
			break
	else:
		print("YES")
	T = T - 1