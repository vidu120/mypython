import math
def factors(a , ans = 0):
	for i in range(1 , math.isqrt(a) + 1):
		if a % i == 0:
			if a // i == i:
				ans = ans + 1
			else:
				ans = ans + 2
	return ans

T = int(input())
while T > 0:
	N = int(input())
	L = []
	for i in range(N-1):
		L.append([int(x) for x in input().split()])
	price = [int(x) for x in input().split()]
	Q = int(input())
	j = 0
	product = 1
	for i in range(Q):
		u , v = [int(x) for x in input().split()]
		if u == v:
			product = price[u-1]
			print(factors(product) % 1000000007)
			continue
		else:
			product = price[u-1]*price[v-1]
		test = L
		b = product
		case = u
		while j < len(test) :
			if test[j][0] == u:
				if test[j][1] == v:
					break
				u = test[j][1]
				product = product * price[test[j][1] - 1]
				case0 = j
				j = 0
			elif test[j][1] == u:
				if test[j][0] == v:
					break
				u = test[j][0]
				product = product * price[test[j][0] - 1]
				case0 = j
				j = 0
			if j == len(test) - 1:
				test.pop(case0)
				product = b
				u = case
				j = -1
			j = j + 1
		print(factors(product) % 1000000007)
	T = T - 1