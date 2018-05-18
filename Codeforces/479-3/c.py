import sys
input = sys.stdin.readline
from collections import Counter
N,K = map(int,input().split())

A = sorted(Counter(list(map(int,input().split()))).items(),key=lambda x: x[0])
def main():
	if K == 0:
		out = min([x[0] for x in A]) - 1
		if out >= 1:
			return out
		else:
			return -1
	cnt = 0
	for x in A:
		cnt += x[1]
		if cnt == K:
			return x[0]
		elif cnt > K:
			return -1
	return -1
print(main())