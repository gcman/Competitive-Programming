from math import sqrt

N = int(input())
M = int(input())

size = int(sqrt(M)) + 1

primes = []
sieve = [True] * (2*10**7 + 1)
for p in range(2, size + 1):
	if sieve[p]:
		primes.append(p)
		for i in range(p, size + 1, p):
			sieve[i] = False
sieve = [True] * (2*10**7 + 1)
sieve[1] = False
for p in primes:
	for i in range((M//p)*p,N-1,-p):
		if i != p:
			sieve[M-i] = False
		
print(sum(sieve[:M-N]))