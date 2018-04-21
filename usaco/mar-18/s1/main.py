fname = "sort"
with open(fname + ".in", "r") as f:
	N = int(f.readline())
	my_list = [int(f.readline()) for x in range(N)]

out = 1+max([x - i for i,x in enumerate([b[0] for b in sorted(enumerate(my_list),key=lambda i:i[1])])])

with open(fname + ".out", "w") as f:
	f.write(str(out))