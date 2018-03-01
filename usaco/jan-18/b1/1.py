with open("billboard.in", "r") as f:
	size = 2000
	plane = [[False for x in range(size + 1)] for y in range(size + 1)]
	lines = [l.strip().split(" ") for l in f.readlines()]
	lx1 = int(lines[0][0])
	ly1 = int(lines[0][1])
	lx2 = int(lines[0][2])
	ly2 = int(lines[0][3])
	cx1 = int(lines[1][0])
	cy1 = int(lines[1][1])
	cx2 = int(lines[1][2])
	cy2 = int(lines[1][3])
	h = ly2 - ly1
	w = lx2 - lx1
	if cx1 <= lx1 and cx2 >= lx2:
		if cy2 >= ly2 and cy1 >= ly1:
			h = cy1 - ly1
		elif cy2 <= ly2 and cy1 <= ly1:
			h = ly2 - cy2
	if cy2 >= ly2 and cy1 <= ly1:
		if cx2 >= lx2 and cx1 >= lx1:
			w = cx1 - lx1
		elif cx2 <= lx2 and cx1 <= lx1:
			w = lx2 - cx2
	if h < 0:
		h = 0
	if w < 0:
		w = 0
with open("billboard.out", "w") as f:
	f.write(str(h*w))