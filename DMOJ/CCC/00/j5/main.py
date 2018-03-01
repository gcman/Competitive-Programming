import sys
input = sys.stdin.readline
n = int(input())

def dfs(graph, start):
	visited, stack = set(), [start]
	while stack:
		node = stack.pop()
		if node not in visited:
			visited.add(node)
			if node not in graph:
				graph[node] = set()
			stack.extend(graph[node] - visited)
	return visited

g = {}
out = []

for i in range(n):
	url = input()
	g[url] = set()
	links = []
	while True:
		line = input()
		if "</HTML>" in line:
			break
		else:
			while "A HREF" in line:
				char = line.find("A HREF") + 8
				link = ""
				while line[char] != '"':
					link += line[char]
					char += 1
				line = line[char:]
				g[url].add(link)

for url in g:
	for link in g[url]:
		out.append("Link from {} to {}".format(url, link))

while True:
	url1 = input()
	if url1 == "The End":
		break
	else:
		url2 = input()
		result = " surf from {} to {}.".format(url1,url2)
		if url2 in dfs(g, url1):
			out.append("Can" + result)
		else:
			out.append("Can't" + result)

for o in out:
	print(o)