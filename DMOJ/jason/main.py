N = int(input())

def modular_exp(n, m):
	power = 2
	out = 1
	while n > 0:
		if n % 2 == 1:
			out = (out * power) % m
		power = (power * power) % m
		n //= 2
	return out

M = 10**9 + 7

print((modular_exp(N+3,M)-5) % M)