P = 1000000007

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
	maximum = n // 2
	for i in range(maximum+1):
		ans = (out[i] * inv(i+1,P) * (n - i)) % P
		out[i+1] = ans
		out[n-i-1] = ans
	return out

def non_empty_matrix(m,n):
	if n > m:
		n,m = m,n
	out = 0
	CHOOSE = choose(n)
	for k in range(n+1):
		to_add = (CHOOSE[k] * pow(pow(2,n-k,P)-1,m,P)) % P
		if k % 2 == 1:
			to_add *= -1
		out = (out + to_add) % P
	return out

T = int(input())
for i in range(T):
	R,C = map(int,input().split())
	print(non_empty_matrix(C,R))