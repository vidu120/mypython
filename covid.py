A = int(input())
while A > 0:
	N = int(input())
	Spots = [int(x) for x in input().split()]
	a = 0
	t = 0
	for i in range(N):
		if Spots[i] == 1:
			if t == 1:
				a = i - a
			if t == 1 and a < 6:
				print("NO")
				break
			a = i
			t = 1
	else:
		print("YES")
	A = A - 1