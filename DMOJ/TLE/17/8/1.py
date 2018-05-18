import sys
input = sys.stdin.readline

N = int(input())
data = [tuple(map(int,input().split())) for _ in range(N)]

def findc(arr):
	for x in arr:
		if x[0] != 0:
			return x[1]/x[0]
	return None

def test(arr):
	C = findc(arr)
	if C == None:
		return all([x[1] == 0 for x in arr])
	else:
		return all([x[1]/x[0] == C for x in arr if x[0] != 0]) and all([x[1] == 0 for x in arr if x[0] == 0]) and all([x[0] == 0 for x in arr if x[1] == 0])

if test(data) == True:
	print("yes")
else:
	print("no")