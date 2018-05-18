P = 2**32 - 5
W = 0

class Tree(object):
	def __init__(self, contents = None):
		if contents is not None:
			self.data = contents
		else:
			self.data = []
			
	def __len__(self):
		return len(self.data)

	def branch(self, n, depth = 0):
		if n >= len(self):
			return []
		start = n
		stop = (2**depth) + n 
		s = self.data[start:stop]
		return s + self.branch(start*2+1, depth+1)

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

def FFT(k,A,w=W): # 2**k values in A, and a primitive root w
	n = 2**k
	if n == 1:
		return [A[0]]
	b = [A[i] for i in range(0,n,2)]
	c = [A[i] for i in range(1,n,2)]
	B = FFT(k-1,b,w**2%P)
	C = FFT(k-1,c,w**2%P)
	y = 1
	out = [0 for i in range(n)]
	for i in range(n//2):
		T = (y * C[i]) % P
		out[i] = (B[i] + T) % P
		out[i+n//2] = (B[i] - T) % P
		y = (y*w)%P
	return out

def FFTMult(k,a,b,w=W):
	n = 2**k
	A = FFT(k,a)
	B = FFT(k,b)
	C = [(A[i]*B[i])%P for i in range(n)]
	C = FFT(k,C,inv(w,P))
	return [x*inv(n,P) for x in C]

print(FFTMult(1,[1,1],[1,1]))

def loc(i,j): # j-th element of i-th row
	return 2**i + j - 1 # Both are 0-indexed

def buildSubProd(k,U): # 2**k leaves in U
	n = 2**k
	out = [None for _ in range(2*n-1)]
	for j in range(n - 2, 2*n - 2):
		out[j+1] = U[j-n+2]
		print(out)
	for i in range(k-1,0,-1):
		for j in range(2**(k-i)):
			out[loc(i,j)] = out[loc(i+1,2*j)]*out[loc(i+1,2*j+1)] # Build parent prod from children
	return out

print(buildSubProd(2,[1,2,3,4]))	