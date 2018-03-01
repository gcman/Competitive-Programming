from sys import stdin, stdout
def dfs(graph, start):
	visited, stack = set(), [start]
	while stack:
		node = stack.pop()
		if node not in visited:
			visited.add(node)
			stack.extend(graph[node])
	return visited

def dfs_paths(graph, start, goal):
	stack = [(start, [start])]
	while stack:
		(node, path) = stack.pop()
		for next in graph[node] - set(path):
			if next == goal:
				yield path + [next]
			else:
				stack.append((next, path + [next]))

n = int(stdin.readline())
g = {}
for i in range(n):
	x,y = map(int, stdin.readline().split())
	g[x] = set()
	g[x].add(y)

while True:
	x,y = map(int, stdin.readline().split())
	if x == 0 and y == 0:
		break
	else:
		if x in dfs(g, x) and y in dfs(g,x):
			sep = list(dfs_paths(g, x, y))[0][1:].index(y)
			stdout.write("Yes " + str(sep) + "\n")
		else:
			stdout.write("No" + "\n")