import sys
input = sys.stdin.readline

Q,K = map(int, input().split())

def bs(arr, x):
	l,r = 0, len(arr) - 1
	while l <= r:
		mid = l + (r - l) // 2
		if arr[mid] == x:
			return (mid,)
		elif arr[mid] < x:
			l = mid + 1
		else:
			r = mid - 1
	return (r,l)

def cnt(arr,m,n):
	l,r = max(0,max(bs(arr,m))), max(0,min(bs(arr,n)))
	if r == 0 and l == 0:
		if arr:
			return int(M <= arr[0] and N >= arr[0])
		else:
			return 0
	return r - l + 1

def cart(lists):
	if lists == []:
		return [()]
	return [x + (y,) for x in cart(lists[:-1]) for y in lists[-1]]

def cartesian(lists):
	return ["".join(map(str, x)) for x in cart(lists)]
	
PAL = [1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99]
for n in range(3,11):
	dig = ["123456789"]
	dig += ["0123456789"]*(n//2 - 1)
	if n % 2 == 1:
		dig.append("0123456789")
	for x in cartesian(dig):
		rev = x[:n//2]
		x += rev[::-1]
		PAL.append(int(x))
PAL = [p for p in PAL if p % K == 0]

for i in range(Q):
	M,N = map(int,input().split())
	print(cnt(PAL,M,N))