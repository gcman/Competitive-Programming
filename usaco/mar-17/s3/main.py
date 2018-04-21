fname = "where"
with open(fname + ".in", "r") as f:
	N = int(f.readline())
	image = [[x for x in f.readline().strip()] for y in range(N)]

def to_num(a,b,c):
	if c == a:
		return 0
	else:
		return 1

def subgrids(arr):
	x = len(arr)
	y = len(arr[0])
	possible = {}
	out = []
	for i in range(0,x-2):
		for j in range(0,y-2):
			possible[(i,j)] = []
	for i in possible:
		for j in range(i[0]+2,x):
			for k in range(i[1]+2,y):
				possible[i].append((j,k))
	for i in possible:
		for j in possible[i]:
			OUT = [[arr[b][a] for a in range(i[1],j[1] + 1)] for b in range(i[0],j[0]+1)]
			LEN = list(set([i for j in OUT for i in j]))
			if len(LEN) == 2:
				out.append([OUT,LEN])
	return out

def find_connected():
	

with open(fname + ".out", "w") as f:
	f.write("0")

def floodfill(arr,start):
	if start == None:
		start = 
	arr = [[to_num(arr[1][0],arr[1][1],j) for j in i] for i in arr[0]]
	w = len(arr)
	h = len(arr[0])
	pos_0 = [(i,j) for j in range(h) for i in range(w) if arr[i][j] == 0]
	pos_1 = [(i,j) for j in range(h) for i in range(w) if arr[i][j] == 1]
	print(pos_0,pos_1)
	seen = set()
	for i in range(w):
		for j in range(h):
			if (i,j) not in seen:
				same = [(i,j)]
				pos = 0
				while pos < len(same):
					x,y = same[pos]
					for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
						if 0 <= x2 < len(arr) and 0 <= y2 < len(arr[x2]) and (x2,y2) not in seen and arr[x2][y2] == arr[i][j]:
							same.append((x2,y2))
							seen.add((x2,y2))
					pos += 1
	return seen