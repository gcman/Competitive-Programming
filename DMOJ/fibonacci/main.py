N = int(input())
M = 1000000007

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
			return (d, (c + d) % M)

print(fib(N)[0])