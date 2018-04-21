from random import randint

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

def choose(n):
	out = [0]*(n+1)
	out[0] = 1
	out[n] = 1
	for i in range(n//2 + 1):
		ans = out[i] // (i+1) * (n - i)
		out[i+1] = ans
		out[n-i-1] = ans
	return out

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def brent(N):
	if N%2==0:
		return 2
	y,c,m = randint(1, N-1),randint(1, N-1),randint(1, N-1)
	g,r,q = 1,1,1
	while g == 1:
		x = y
		for _ in range(r):
			y = ((y*y)%N+c)%N
		k = 0
		while (k<r and g==1):
			ys = y
			for _ in range(min(m,r-k)):
				y = ((y*y)%N+c)%N
				q = q*(abs(x-y))%N
			g = gcd(q,N)
			k = k + m
		r = r*2
	if g == N:
		while True:
			ys = ((ys*ys)%N+c)%N
			g = gcd(abs(x-ys),N)
			if g > 1:
				break
	return g

def crt(n,a,M):
	S = 0
	for n_i, a_i in zip(n, a):
		p = M // n_i
		S += a_i * inv(p, n_i) * p
	return S % M

N,M = map(int,input().split())
prime_pow = []
mod_prime_pow = []
while M > 1:
	B = brent(M)
	out = 1
	while M % B == 0:
		out *= B
		M //= B
	prime_pow.append(out)
for p in prime_pow:
	print(choose(N))