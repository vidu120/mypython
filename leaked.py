T = int(input())
while T > 0:
	N , M , K = [int(x) for x in input().split()]
	while N > 0:
		L = [int(x) for x in input().split()]
		max_que = 0
		ans= 1
		for i in range(M):
			max_que = max(max_que , L.count(i+1))
			if max_que == L.count(i + 1):
				ans = i+1
		print(ans , end = ' ')
		N = N - 1
	print()
	T = T - 1