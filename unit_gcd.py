T = int(input())
while T > 0:
	N = int(input())
	if N == 1:
		print("1")
		print("1 1")
	elif N == 2:
		print("1")
		print("2 1 2")
	else:	
		if N % 2 != 0:
			print((N-1) // 2)
			print(F"3 1 2 {N}")
			for i in range(3 ,N, 2):
				print(f"2 {i} {i+1}")
		else:
			print(N//2)
			for i in range(1 , N , 2):
				print(f"2 {i} {i + 1}")
	T = T - 1