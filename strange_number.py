test = int(input())
while test > 0:
	a , b = map(int , input().split())
	L =[]
	if a >= 2**b:
		while True:
			if a % 2 != 0:
				break
			L.append(2)
			a = a / 2
		for i in range(3 , int(sqrt(a)) , 2):
			


		print(1)
	else:
		print(0)
	test = test -1