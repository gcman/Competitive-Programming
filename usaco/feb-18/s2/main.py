fname = "snowboots"
with open(fname + ".in", "r") as f:
	N,B = map(int, f.readline().split())
	depth = [x for x in list(map(int, f.readline().split()))]
	boot_depth = []
	boot_step = []
	for i in range(B):
		d,s = map(int, f.readline().split())
		boot_depth.append(d)
		boot_step.append(s)

visited = [[False for i in range(B)] for j in range(N)]
def visit(n,b):
	if visited[n][b] == True:
		return
	else:
		visited[n][b] = True
	if n == N - 1:
		return
	for i in range(n+1,n+boot_step[b]+1):
		if i < N:
			if boot_depth[b] >= depth[i]:
				visit(i,b)
	for j in range(b+1,B):
		if boot_depth[j] >= depth[n]:
			visit(n,j)
visit(0,0)
ans = 9999
for i,x in enumerate(visited[N-1]):
	if x == True:
		ans = i
		break

with open(fname + ".out", "w") as f:
	f.write(str(ans))