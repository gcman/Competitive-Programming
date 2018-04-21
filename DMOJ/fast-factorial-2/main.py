import sys
N = int(sys.stdin.readline())
P = 2**32 - 5
lower = 1
F = 1
A = [int(sys.stdin.readline()) for i in range(N)]
A = sorted(enumerate(A), key=lambda x: P - x[1] - 1 if x[1] >= 2 ** 31 else x[1])

def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)

def inv(a, m):
	g, x, y = egcd(a, m)
	if g != 1:
		return None
	else:
		return x % m

def f(n):
	global F,lower
	if n >= P:
		return 0
	elif n >= P // 2:
		ans = P + f(P - n - 1)
		if n % 2 == 0:
			ans *= -1
		return inv(ans,P)
	else:
		F = (F * prod((range(lower+1,n+1)))) % P
		lower = n
		return F

def prod(arr):
	length = len(arr)
	out = 1
	for i in arr:
		out = (out * i) % P
	return out

out = [0]*N
for i,x in A:
	out[i] = f(x)
for x in out:
	print(x)