import itertools
T = int(input())
while T > 0:
	N = int(input())
	L = [abs(int(x)) for x in input().split()]
	ans = (N * (N + 1))//2
	for i in range(0,N,1):
		if L[i] % 2 != 0:
			for j in range(i+1,N,1):
				if L[j] % 4 == 0:
					break
				if L[j] % 2 == 0:
					for k in range(j + 1, N , 1):
						if L[k] % 2 == 0:
							ans = ans - (k - j + 1)
							break
						if k == N - 1:
							ans = ans - (k - j + 1)
					break
		elif L[i] % 4 != 0:
			for j in range(i , N , 1):
				if j == N - 1:
					ans = ans - (j-i + 1)
					continue
				if j == i:
					continue
				if L[j] % 2 == 0:
					ans = ans - (j-i)
					break
	print(ans)
	T = T - 1