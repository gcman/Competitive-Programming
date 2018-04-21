full = set([])
half = set([])
N = int(input())
for i in range(N):
	X,Y,D = map(int, input().split())
	for i in range(D):
		for j in range(X+D-i,X,-1):
			fill = (j-1,Y+i)
			if j == X + D - i:
				if fill not in full:
					half.add(fill)
			else:
				full.add(fill)
				half.discard(fill)
print((2*len(full) + len(half)) / 2)