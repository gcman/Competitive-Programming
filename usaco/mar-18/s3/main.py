with open("multimoo.in", "r") as f:
	N = int(f.readline())
	board = [[y for y in map(int,f.readline().split())] for x in range(N)]

def neighbours(tup):
	i = tup[0]
	j = tup[1]
	return [x for x in [(i-1,j),(i,j-1),(i+1,j),(i,j+1)] if 0 <= x[0] and N > x[0] and 0 <= x[1] and N > x[1]]

def b(node):
	return board[node[0]][node[1]]

g = {}
G = {}
seen = set()

def dfs(start,flood):
	global g,seen,G
	extra_neighbour_types = set()
	visited, stack = set(), [start]
	f1 = b(start)
	while stack:
		node = stack.pop()
		if flood != -1:
			if node in G:
				seen |= G[node]
		if node not in visited and node not in seen:
			visited.add(node)
			real = []
			for x in neighbours(node):
				if flood == -1:
					if b(x) == f1:
						real.append(x)
					else:
						extra_neighbour_types.add(b(x))
				else:
					if b(x) in [f1,flood]:
						real.append(x)
					else:
						extra_neighbour_types.add(b(x))
			stack.extend(real)
	if flood == -1:
		if node not in seen and node not in g:
			g[node] = tuple(extra_neighbour_types)
			seen |= visited
		elif node not in G:
			G[node] = visited
	elif node in G:
		seen |= G[node]
	return visited

mx1 = max([len(dfs((i,j),-1)) for i in range(N) for j in range(N)])
seen = set()
out = []
for x in g:
	for y in g[x]:
		out.append(len(dfs(x,y)))

mx2 = max(out)

#print(mx1,mx2)

with open("multimoo.out", "w") as f:
	f.write(str(mx1)+"\n")
	f.write(str(mx2))