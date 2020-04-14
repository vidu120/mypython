def find(p , q  , m = 998244353 , i = 1):
	while True:
		if ((p%m) + m * i) % q == 0:
			print(((p%m) + m*i)//q)
			break
		i = i + 1
T = int(input())
while T > 0:
	l = input()
	for i in l:
		