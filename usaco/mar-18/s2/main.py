fname = "lemonade"
with open(fname + ".in", "r") as f:
	N = int(f.readline())
	cows = list(map(int, f.readline().strip().split()))

line = 0
for x in sorted(cows,reverse=True):
	if x >= line:
		line += 1
	else:
		break

with open(fname + ".out", "w") as f:
	f.write(str(line))
