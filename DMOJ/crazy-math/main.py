A,B,N = map(int,input().split())
M = 1000000000

def fib(n):
	if n == 0:
		return (0,1)
	else:
		a,b = fib(n // 2)
		c = (a * (2*b - a)) % M
		d = (a*a + b*b) % M
		if n % 2 == 0:
			return (c, d)
		else:
			return (d, (c + d))
if N == 0:
	print(A)
else:
	F = fib(N-1)
	print((A*F[0] + B*F[1] + M)%M)