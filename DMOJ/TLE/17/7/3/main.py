import sys
input = sys.stdin.readline
Q = int(input())

def tetr(x,y,z):
	exp = x
	for _ in range(y-1):
		try:
			exp = x ** exp
		except OverflowError as err:
			return z + 1
	return exp

def bin(y,z):
	lower = 1
	upper = 10
	while True:
		mid = (lower + upper)/2
		if tetr(mid,y,z) > z:
			upper = mid
			if tetr(mid-10e-6,y,z) < z:
				break
		else:
			lower = mid
			if tetr(mid+10e-6,y,z) > z:
				break
	return mid

for _ in range(Q):
	Y,Z = map(int, input().split())
	print(bin(Y,Z))