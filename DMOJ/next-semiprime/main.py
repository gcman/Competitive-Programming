from sys import stdin
from random import randint
input = stdin.readline

def gcd(a, b):
	a = abs(a)
	b = abs(b)
	while a:
		a, b = b % a, a
	return b

def brent(N):
	if N % 2 == 0:
		return 2
	y, c, m = randint(1, N - 1), randint(1, N - 1), randint(1, N - 1)
	g, r, q = 1, 1, 1
	while g == 1:
		x = y
		for i in range(r):
			y = ((y * y) % N + c) % N
		k = 0
		while k < r and g == 1:
			ys = y
			for i in range(min(m, r - k)):
				y = ((y * y) % N + c) % N
				q = q * (abs(x - y)) % N
			g = gcd(q, N)
			k = k + m
		r *= 2
	if g == N:
		while True:
			ys = ((ys * ys) % N + c) % N
			g = gcd(abs(x - ys), N)
			if g > 1:
				break
	return g

def miller_rabin_pass(a, s, d, n):
	apow = pow(a, d, n)
	if apow == 1:
		return True
	for i in range(s-1):
		if apow == n - 1:
			return True
		apow = (apow * apow) % n
	return apow == n - 1

def miller_rabin(n):
	if n < 2:
		return False
	if n in [2, 7, 61]:
		return True
	d = n - 1
	s = 0
	while d % 2 == 0:
		d >>= 1
		s += 1
	for a in [2,7,61]:
		if not miller_rabin_pass(a, s, d, n):
			return False
	return True

def is_semiprime(n):
	if miller_rabin(n):
		return False
	B = brent(n)
	while B == n:
		B = brent(n)
	return miller_rabin(B) and miller_rabin(n//B)

def next_semiprime(n):
	n += 1
	while not is_semiprime(n):
		n += 1
	return n

for _ in range(int(input())):
	print(next_semiprime(int(input())))