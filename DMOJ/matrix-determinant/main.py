import sys
input = sys.stdin.readline
M = 1000000007
N = int(input())
A = [[int(x) for x in input().split()] for j in range(N)]

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

def determinant(a):
	n = len(a)
	det = 1
	for i in range(n - 1):
		k = i
		for j in range(i + 1, n):
			if abs(a[j][i]) > abs(a[k][i]):
				k = j
		if k != i:
			a[i], a[k] = a[k], a[i]
			det = -det
		for j in range(i + 1, n):
			t = a[j][i] * inv(a[i][i],M)
			for k in range(i + 1, n):
				a[j][k] = (a[j][k] - (t*a[i][k]) % M) % M
	for i in range(n - 1, -1, -1):
		det = (det * a[i][i]) % M
	return int(det)

print((determinant(A) + M) % M)