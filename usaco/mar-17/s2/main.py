fname = "cownomics"
with open(fname + ".in", "r") as f:
	N,M = map(int, f.readline().split())
	spotted = [[x for x in f.readline().strip()] for j in range(N)]
	plain = [[x for x in f.readline().strip()] for j in range(N)]

ans = set([])
def search(i,j,k):
	if i == j or i == k or j == k:
		return
	seen = set([])
	for n in range(N):
		seen.add((spotted[n][i],spotted[n][j],spotted[n][k]))
	for n in range(N):
		if (plain[n][i],plain[n][j],plain[n][k]) in seen:
			return
	ans.add(tuple(sorted([i,j,k])))

for i in range(M):
	for j in range(M):
		for k in range(M):
			search(i,j,k)

with open(fname + ".out", "w") as f:
	f.write(str(len(ans)))