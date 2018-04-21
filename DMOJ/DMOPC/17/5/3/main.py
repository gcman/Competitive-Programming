from sys import stdin

input = stdin.readline
N = int(input())
A = list(map(int, input().split()))

def gcd(a,b):
	r = a % b
	while r:
		a = b
		b = r
		r = a % b
	return b

def LPF(n):
	while n % 2 == 0:
		lpf = 2
		n //= 2
	i = 3
	while i * i < n + 1:
		while n % i == 0:
			lpf = i
			n = n // i
		i += 2
	if n > 2:
		lpf = n
	return lpf

GCD = gcd(A[0],A[1])

for i in range(2,N):
	GCD = gcd(GCD,A[i])

if GCD == 1:
	print("DNE")
else:
	print(LPF(GCD))