test = int(input())
while test > 0:
	N = int(input())
	p = [int(x) for x in input().split()]
	p.sort(reverse = True)
	smax = 0
	for i in range(N):
		p[i] = p[i] - i
		if p[i] < 0:
			p[i] = 0
		smax += p[i]
	smax = smax % 1000000007 
	print(smax)
	test = test - 1