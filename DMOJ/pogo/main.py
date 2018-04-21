N,M = map(int,input().split())
P = 1000000007
if M == 1:
	print(1)
elif M == 2:
	paths = [0]*(N+1)
	paths[1] = 1
	paths[2] = 1
	for i in range(3,N+1):
		paths[i] = (paths[i-1] + paths[i-3]) % P
	print(paths[N])
elif M == 3:
	def A(n):
		if n <= 0:
			return 1
		return (A(n-1) + A(n-5) + B(n-2) + B(n-3)) % P
	def B(n):
		if n <= 0:
			return 0
		return (A(n-1) + A(n-2) + B(n-3) + D(n-1) + D(n-3)) % P
	def D(n):
		if n <= 0:
			return 0
		return (A(n) + A(n-3) + D(n-2) + D(n-4) + B(n-4)) % P
	print(A(N))