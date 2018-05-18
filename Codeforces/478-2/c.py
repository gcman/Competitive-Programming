import sys
input = sys.stdin.readline

N,Q = map(int,input().split())
A = list(map(int,input().split()))
K = list(map(int,input().split()))

psum = []
smax = 0
for x in A:
	smax += x
	psum.append(smax)
A = psum

def bs(arr, x):
	l,r = 0, len(arr) - 1
	while l <= r:
		mid = l + (r - l) // 2
		if arr[mid] == x:
			return mid
		elif arr[mid] < x:
			l = mid + 1
		else:
			r = mid - 1
	return r

deaths = 0
wasted = 0
max_dmg = A[N-1]
dmg = 0

for x in K:
	dmg += x
	X = dmg
	X -= wasted
	X -= deaths*max_dmg
	if X >= max_dmg:
		wasted += X - max_dmg
		deaths += 1
		ans = N
	else:
		ans = N - 1 - bs(A,X)
	print(ans)