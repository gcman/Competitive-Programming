from math import sqrt

N = int(input())
cost = 0

while N > 1:
	r = int(sqrt(N)) + 1
	factor = 2
	while factor <= r and N % factor != 0:
		factor += 1
	if factor < N and N % factor == 0:
		increment = N // factor
		N -= increment
		cost += N // increment
	else:
		N -= 1
		cost += N
print(cost)