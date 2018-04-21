import sys
input = sys.stdin.readline
M = 1000000007
N = int(input())
A = [[int(x) for x in input().split()] for j in range(N)]
det = 1

for i in range(N):
	maxind = i
	for j in range(i+1,N):
		if A[j][i] > A[maxind][i]:
			maxind = j
	if maxind != i:
		det = -det
		A[i],A[maxind] = A[maxind],A[i]
	for j in range(i+1,N):
		X = A[j][i] * pow(A[i][i],M-2,M)
		for k in range(i,N):
			A[j][k] = (A[j][k] - X*A[i][k] + M) % M
for i in range(N):
	det = (det * A[i][i]) % M
print((det + M) % M)