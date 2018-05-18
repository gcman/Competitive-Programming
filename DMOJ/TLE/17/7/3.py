import sys
#sys.stdin = open("data.txt")
input = sys.stdin.readline

Q = int(input())
ERR = 1e-6

def tetr(a,b,z):
	aorig = a
	for _ in range(b-1):
		try:
			a = aorig ** a
		except OverflowError as err:
			return z + 1
	return a

def bs(y,z):
	l,r = 1, 10
	while True:
		mid = l + (r - l) / 2
		ANS = tetr(mid,y,z)
		if ANS < z:
			if tetr(mid + ERR,y,z) > z:
				return mid
			l = mid
		elif ANS > z:
			if tetr(mid - ERR,y,z) < z:
				return mid
			else:
				r = mid

for _ in range(Q):
	Y,Z = map(int,input().split())
	print(bs(Y,Z))