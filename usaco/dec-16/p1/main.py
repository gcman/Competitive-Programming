with open("triangles.in","r") as f:
	N = int(f.readline())
	trees = [tuple(map(int, f.readline().split())) for i in range(N)]

def area(arr): # Use shoelace theorem
	n = len(arr)
	A = abs(sum([arr[i][0]*arr[i+1][1] - arr[i+1][0]*arr[i][1] for i in range(n-1)]) + arr[n-1][0]*arr[0][1] - arr[0][0]*arr[n-1][1])
	return A / 2

def combinations(iterable, r):
	# combinations('ABCD', 2) --> AB AC AD BC BD CD
	# combinations(range(4), 3) --> 012 013 023 123
	pool = tuple(iterable)
	n = len(pool)
	if r > n:
		return
	indices = list(range(r))
	yield tuple(pool[i] for i in indices)
	while True:
		for i in reversed(range(r)):
			if indices[i] != i + n - r:
				break
		else:
			return
		indices[i] += 1
		for j in range(i+1, r):
			indices[j] = indices[j-1] + 1
		yield tuple(pool[i] for i in indices)

print(list(combinations(range(1000),3)))

#with open("triangles.out"."w") as f: