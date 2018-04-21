fname = "pairup"
with open(fname + ".in", "r") as f:
	N = int(f.readline())
	cows = []
	for i in range(N):
		x,y = map(int, f.readline().split())
		cows.append([x,y])
cows = sorted(cows,key=lambda x: x[1])
mn = 0
mx = N-1
t = []
while cows[mn][0] > 0 or cows[mx][0] > 0:
	pair = min(cows[mn][0],cows[mx][0])
	t.append(cows[mn][1] + cows[mx][1])
	cows[mn][0] -= pair
	cows[mx][0] -= pair
	if cows[mn][0] <= 0:
		mn += 1
	if cows[mx][0] <= 0:
		mx -= 1
with open(fname + ".out", "w") as f:
	f.write(str(max(t)))