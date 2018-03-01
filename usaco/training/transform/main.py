"""
ID: manga1
LANG: PYTHON3
TASK: transform
"""
with open("transform.in","r") as f:
	n = int(f.readline())
	before = [[char for char in f.readline().strip()] for i in range(n)]
	after = [[char for char in f.readline().strip()] for i in range(n)]

def rotate(a):
	return [list(k) for k in list(zip(*reversed(a)))]

def reflect(a):
	return [list(reversed(k)) for k in a]

def find_transform(b,a):
	if a == rotate(b):
		return 1
	elif a == rotate(rotate(b)):
		return 2
	elif a == rotate(rotate(rotate(b))):
		return 3
	elif a == reflect(b):
		return 4
	elif a in [rotate(reflect(b)),rotate(rotate(reflect(b))),rotate(rotate(rotate(reflect(b))))]:
		return 5
	elif a == b:
		return 6
	else:
		return 7

with open("transform.out","w") as f:
	f.write("{}".format(find_transform(before,after)) + "\n")